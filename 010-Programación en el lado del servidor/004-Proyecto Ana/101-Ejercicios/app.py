from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import queue
import uuid
import os
import tempfile

app = Flask(__name__)

sesiones = {}

class SesionPython:

    def __init__(self, codigo):

        fd, ruta = tempfile.mkstemp(suffix=".py", prefix="laboratorio_")
        os.write(fd, codigo.encode("utf-8"))
        os.close(fd)

        self.ruta = ruta

        self.proceso = subprocess.Popen(
            ["python", self.ruta],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        self.cola = queue.Queue()
        self.activa = True

        self.hilo = threading.Thread(
            target=self.leer_salida,
            daemon=True
        )

        self.hilo.start()

    def leer_salida(self):

        try:

            for linea in self.proceso.stdout:
                self.cola.put(linea)

            errores = self.proceso.stderr.read()

            if errores:
                self.cola.put(errores)

        finally:

            self.proceso.wait()
            self.activa = False

            try:
                os.remove(self.ruta)
            except:
                pass

    def escribir(self, texto):

        if not self.activa:
            return

        try:
            self.proceso.stdin.write(texto + "\n")
            self.proceso.stdin.flush()
        except:
            self.activa = False

    def leer_todo(self):

        salida = []

        while not self.cola.empty():

            salida.append(self.cola.get_nowait())

        return "".join(salida)

    def esta_activa(self):

        return self.activa and self.proceso.poll() is None


@app.route("/")
def inicio():
    return render_template("laboratorio.html")

@app.route("/api/start", methods=["POST"])
def iniciar_codigo():

    datos = request.get_json(force=True)

    codigo = datos.get("code", "")

    id_sesion = str(uuid.uuid4())

    sesiones[id_sesion] = SesionPython(codigo)

    return jsonify({
        "session_id": id_sesion
    })


@app.route("/api/write", methods=["POST"])
def escribir_entrada():

    datos = request.get_json(force=True)

    id_sesion = datos.get("session_id")
    linea = datos.get("line", "")

    sesion = sesiones.get(id_sesion)

    if not sesion:
        return jsonify({
            "error": "Sesión no encontrada"
        }), 404

    sesion.escribir(linea)

    return jsonify({
        "ok": True
    })


@app.route("/api/read", methods=["GET"])
def leer_terminal():

    id_sesion = request.args.get("session_id")

    sesion = sesiones.get(id_sesion)

    if not sesion:
        return jsonify({
            "error": "Sesión no encontrada"
        }), 404

    salida = sesion.leer_todo()
    activa = sesion.esta_activa()

    if not activa and not salida:
        sesiones.pop(id_sesion, None)

    return jsonify({
        "output": salida,
        "alive": activa
    })


if __name__ == "__main__":
    app.run(debug=True)