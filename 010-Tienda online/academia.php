<?php

$host = "localhost";
$user = "root";
$pass = "";
$db   = "academiaonline";

$conexion = new mysqli($host, $user, $pass, $db);

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

?>
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Academia Nova</title>

    <style>
        body, html {
            background: mediumseagreen;
            font-family: sans-serif;
            margin: 0;
            padding: 0;
        }

        header, main, footer {
            width: 800px;
            background: white;
            padding: 20px;
            margin: auto;
        }

        header {
            text-align: center;
        }

        nav ul {
            display: flex;
            width: 100%;
            justify-content: center;
            list-style-type: none;
            padding: 0;
            margin: 0;
            gap: 20px;
        }

        nav ul li {
            padding: 0;
            margin: 0;
        }

        nav a {
            color: seagreen;
            text-decoration: none;
            font-weight: bold;
        }

        #heroe {
            background: seagreen;
            height: 400px;
            display: flex;
            flex-direction: column;
            color: white;
            justify-content: center;
            align-items: center;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }

        #heroe a {
            color: seagreen;
            background: white;
            text-decoration: none;
            padding: 10px;
            border-radius: 5px;
        }

        #razones {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        #razones article {
            text-align: center;
            background: seagreen;
            padding: 20px;
            border-radius: 5px;
            display: flex;
            flex-direction: column;
            color: white;
            justify-content: center;
            align-items: center;
        }

        #catalogo {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        #catalogo article {
            background: #f1f1f1;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
        }

        .imagen {
            width: 100%;
            height: 120px;
            background: seagreen;
            border-radius: 5px;
            margin-bottom: 10px;
        }

        .boton {
            display: inline-block;
            background: seagreen;
            color: white;
            text-decoration: none;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }

        .caja {
            background: #f1f1f1;
            padding: 30px;
            border-radius: 5px;
            text-align: center;
        }

        footer {
            text-align: center;
        }
    </style>
</head>

<body>

<header>
    <h1>Academia Nova</h1>
    <h2>Cursos online para aprender desde casa</h2>

    <nav>
        <ul>
            <li><a href="academia.php">Inicio</a></li>
            <li><a href="?pagina=catalogo">Catálogo</a></li>
        </ul>
    </nav>
</header>

<main>

<?php

if (isset($_GET['pagina'])) {

    if ($_GET['pagina'] == "catalogo") {

        echo "<h2>Catálogo de cursos</h2>";
        echo "<section id='catalogo'>";

        $sql = "SELECT * FROM curso;";
        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
            echo "
                <article>
                    <div class='imagen'></div>
                    <h3>".$fila['nombre_curso']."</h3>
                    <p>".$fila['precio']." €</p>
                    <p>".$fila['descripcion']."</p>
                    <p>Plazas disponibles: ".$fila['plazas']."</p>
                    <a class='boton' href='?pagina=curso&id=".$fila['id']."'>Ver curso</a>
                </article>
            ";
        }

        echo "</section>";
    }

    else if ($_GET['pagina'] == "curso") {

        $id = $_GET['id'];

        $sql = "SELECT * FROM curso WHERE id = ".$id.";";
        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
            echo "
                <section class='caja'>
                    <h2>".$fila['nombre_curso']."</h2>
                    <p>".$fila['descripcion']."</p>
                    <p>Precio: ".$fila['precio']." €</p>
                    <p>Plazas disponibles: ".$fila['plazas']."</p>
                    <a class='boton' href='?pagina=inscripcion'>Inscribirme</a>
                </section>
            ";
        }
    }

    else if ($_GET['pagina'] == "inscripcion") {
        echo "
            <section class='caja'>
                <h2>Esta es la página de inscripción</h2>
                <p>Ya casi estás dentro del curso.</p>
                <a class='boton' href='?pagina=finalizacion'>Vamos a finalizar la inscripción</a>
            </section>
        ";
    }

    else if ($_GET['pagina'] == "finalizacion") {
        echo "
            <section class='caja'>
                <h2>Inscripción finalizada</h2>
                <p>Tu inscripción se ha realizado correctamente.</p>
                <a class='boton' href='academia.php'>Ya has acabado, vamos a volver a empezar</a>
            </section>
        ";
    }

} else {

?>

<section id="heroe">
    <h3>Aprende algo nuevo sin moverte de casa</h3>
    <p>Elige un curso y empieza poco a poco con ejemplos prácticos.</p>
    <a href="?pagina=catalogo">Vamos a ver el catálogo de cursos</a>
</section>

<section id="razones">
    <article>
        <h4>Clases sencillas</h4>
        <p>Los cursos están pensados para aprender desde cero.</p>
    </article>

    <article>
        <h4>Ejercicios prácticos</h4>
        <p>Cada tema incluye ejemplos para practicar.</p>
    </article>

    <article>
        <h4>Aprendizaje online</h4>
        <p>Puedes estudiar desde casa y a tu ritmo.</p>
    </article>

    <article>
        <h4>Contenido útil</h4>
        <p>Los cursos están orientados a proyectos reales.</p>
    </article>
</section>

<?php

}

$conexion->close();

?>

</main>

<footer>
    <p>Academia Nova - Proyecto de clase</p>
</footer>

</body>
</html>