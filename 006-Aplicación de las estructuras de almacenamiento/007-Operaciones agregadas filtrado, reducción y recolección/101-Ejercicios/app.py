import random
from flask import Flask, render_template

app = Flask(__name__)

# =========================
# VALIDACIÓN DE REGLAS
# =========================

def es_valido(grid, fila, col, num):

    # Comprobar fila
    if num in grid[fila]:
        return False

    # Comprobar columna
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Comprobar bloque 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3

    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_col, inicio_col + 3):
            if grid[f][c] == num:
                return False

    return True


# =========================
# BACKTRACKING
# =========================

def resolver_sudoku(grid):

    for fila in range(9):
        for col in range(9):

            if grid[fila][col] == 0:

                opciones = list(range(1, 10))
                random.shuffle(opciones)

                for num in opciones:

                    if es_valido(grid, fila, col, num):

                        grid[fila][col] = num

                        if resolver_sudoku(grid):
                            return True

                        grid[fila][col] = 0

                return False

    return True


# =========================
# GENERADOR
# =========================

def generar_sudoku():

    grid = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(grid)
    return grid


# =========================
# CONVERSIÓN A BLOQUES
# =========================

def a_bloques(sudoku):

    bloques = []

    for br in range(3):
        for bc in range(3):

            bloque = []

            for f in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    bloque.append(sudoku[f][c])

            bloques.append(bloque)

    return bloques


# =========================
# RUTA WEB
# =========================

@app.route("/")
def inicio():

    sudoku = generar_sudoku()
    datos = a_bloques(sudoku)

    return render_template("index.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)