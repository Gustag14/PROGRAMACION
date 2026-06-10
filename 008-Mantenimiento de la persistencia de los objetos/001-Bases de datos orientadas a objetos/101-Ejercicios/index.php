<!doctype html>
<html lang="es">
<head>
    <title>Cafetería Online</title>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f1ed;
        }

        header {
            background: #3b2f2f;
            color: white;
            padding: 15px;
            text-align: center;
        }

        main {
            padding: 15px;
        }

        section {
            background: white;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 10px;
        }

        article {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 8px;
            border-radius: 6px;
        }

        button, #enviar {
            background: #3b2f2f;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 8px;
            box-sizing: border-box;
        }

        footer {
            text-align: center;
            padding: 10px;
            font-size: 12px;
        }
    </style>
</head>

<body>

<header>
    <h1>Cafetería Online</h1>
</header>

<main>

    <section id="productos">
        <h3>Productos disponibles</h3>

        <div>
            <?php
            $host = "localhost";
            $user = "root";
            $pass = "";
            $db   = "microtienda";

            $conexion = new mysqli($host, $user, $pass, $db);

            $sql = "SELECT * FROM productos;";
            $resultado = $conexion->query($sql);

            while ($fila = $resultado->fetch_assoc()) {
            ?>
                <article>
                    <h4><?= $fila['nombre'] ?></h4>
                    <button
                        data-nombre="<?= $fila['nombre'] ?>"
                        data-precio="<?= $fila['precio'] ?>">
                        Añadir <?= $fila['precio'] ?>€
                    </button>
                </article>
            <?php } ?>
        </div>
    </section>

    <section>
        <h3>Datos del cliente</h3>

        <input type="text" id="nombre" placeholder="Nombre">
        <input type="text" id="apellidos" placeholder="Apellidos">
        <input type="text" id="email" placeholder="Email">

        <div id="enviar">Confirmar pedido</div>
    </section>

</main>

<footer>
    Cafetería Online - 2026
</footer>

<script>
    let pedido = {
        cliente: {},
        productos: [],
        pedido: {
            numero: Date.now(),
            fecha: new Date().toISOString().slice(0, 10)
        }
    };

    let botones = document.querySelectorAll("button");

    botones.forEach(function(boton) {

        boton.onclick = function() {

            pedido.productos.push({
                nombre: this.dataset.nombre,
                precio: this.dataset.precio
            });

            console.log("Producto añadido:", pedido);
        };

    });

    let enviar = document.querySelector("#enviar");

    enviar.onclick = function() {

        pedido.cliente = {
            nombre: document.querySelector("#nombre").value,
            apellidos: document.querySelector("#apellidos").value,
            email: document.querySelector("#email").value
        };

        fetch("guardamongo.php", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(pedido)
        })
        .then(respuesta => respuesta.json())
        .then(datos => {
            console.log("Respuesta MongoDB:", datos);
            alert("Pedido enviado correctamente");
        });

    };
</script>

</body>
</html>