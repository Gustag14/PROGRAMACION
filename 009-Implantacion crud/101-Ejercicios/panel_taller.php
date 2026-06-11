<?php

// ===============================
// CONEXIÓN A LA BASE DE DATOS
// ===============================

$host = "localhost";
$user = "root";
$pass = "";
$db   = "taller_informatico";

$conexion = new mysqli($host, $user, $pass, $db);

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}


// ===============================
// CREAR INCIDENCIA
// ===============================

if (isset($_POST['crear'])) {

    $cliente = $_POST['cliente'];
    $equipo = $_POST['equipo'];
    $problema = $_POST['problema'];
    $fecha = $_POST['fecha'];

    $sql = "
        INSERT INTO incidencias VALUES (
            NULL,
            '".$cliente."',
            '".$equipo."',
            '".$problema."',
            '".$fecha."'
        );
    ";

    $conexion->query($sql);

    header("Location: panel_taller.php");
}


// ===============================
// ACTUALIZAR INCIDENCIA
// ===============================

if (isset($_POST['actualizar'])) {

    $id = $_POST['id'];
    $cliente = $_POST['cliente'];
    $equipo = $_POST['equipo'];
    $problema = $_POST['problema'];
    $fecha = $_POST['fecha'];

    $sql = "
        UPDATE incidencias
        SET
            cliente = '".$cliente."',
            equipo = '".$equipo."',
            problema = '".$problema."',
            fecha = '".$fecha."'
        WHERE id = ".$id.";
    ";

    $conexion->query($sql);

    header("Location: panel_taller.php");
}


// ===============================
// ELIMINAR INCIDENCIA
// ===============================

if (isset($_GET['accion']) && $_GET['accion'] == "eliminar") {

    $id = $_GET['id'];

    $sql = "DELETE FROM incidencias WHERE id = ".$id.";";

    $conexion->query($sql);

    header("Location: panel_taller.php");
}

?>

<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel del taller informático</title>

    <style>
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            display: flex;
            background: #f2f2f2;
        }

        nav {
            flex: 1;
            background: #263238;
            color: white;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        nav h2 {
            margin-top: 0;
        }

        nav a {
            background: white;
            color: #263238;
            padding: 10px;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
        }

        main {
            flex: 4;
            padding: 25px;
            background: white;
            position: relative;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            border: 1px solid #263238;
        }

        th {
            background: #263238;
            color: white;
        }

        th, td {
            padding: 8px;
            border: 1px solid #ccc;
        }

        .editar, .eliminar {
            display: inline-block;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            color: white;
            text-align: center;
            line-height: 25px;
            text-decoration: none;
        }

        .editar {
            background: #0277bd;
        }

        .eliminar {
            background: #c62828;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
            max-width: 500px;
        }

        .controlformulario {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        input, textarea {
            padding: 10px;
            border: 1px solid #aaa;
            border-radius: 5px;
        }

        input[type="submit"] {
            background: #263238;
            color: white;
            cursor: pointer;
        }

        #nuevo {
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: #263238;
            color: white;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            text-align: center;
            line-height: 35px;
            text-decoration: none;
            font-size: 28px;
            font-weight: bold;
        }
    </style>
</head>

<body>

<nav>
    <h2>Taller</h2>
    <a href="panel_taller.php">Incidencias</a>
    <a href="?accion=nuevo">Nueva incidencia</a>
</nav>

<main>

<?php

// ===============================
// ROUTER
// ===============================

if (isset($_GET['accion'])) {

    // ===============================
    // FORMULARIO PARA CREAR
    // ===============================

    if ($_GET['accion'] == "nuevo") {
        ?>

        <h1>Nueva incidencia</h1>

        <form action="panel_taller.php" method="POST">

            <div class="controlformulario">
                <label for="cliente">Nombre del cliente</label>
                <input type="text" name="cliente" id="cliente">
            </div>

            <div class="controlformulario">
                <label for="equipo">Equipo afectado</label>
                <input type="text" name="equipo" id="equipo">
            </div>

            <div class="controlformulario">
                <label for="problema">Problema detectado</label>
                <textarea name="problema" id="problema"></textarea>
            </div>

            <div class="controlformulario">
                <label for="fecha">Fecha de entrada</label>
                <input type="text" name="fecha" id="fecha">
            </div>

            <input type="submit" name="crear" value="Guardar incidencia">

        </form>

        <?php
    }


    // ===============================
    // FORMULARIO PARA EDITAR
    // ===============================

    else if ($_GET['accion'] == "editar") {

        $id = $_GET['id'];

        $sql = "SELECT * FROM incidencias WHERE id = ".$id.";";
        $resultado = $conexion->query($sql);

        while ($fila = $resultado->fetch_assoc()) {
            ?>

            <h1>Editar incidencia</h1>

            <form action="panel_taller.php" method="POST">

                <input type="hidden" name="id" value="<?= $fila['id'] ?>">

                <div class="controlformulario">
                    <label for="cliente">Nombre del cliente</label>
                    <input type="text" name="cliente" id="cliente" value="<?= $fila['cliente'] ?>">
                </div>

                <div class="controlformulario">
                    <label for="equipo">Equipo afectado</label>
                    <input type="text" name="equipo" id="equipo" value="<?= $fila['equipo'] ?>">
                </div>

                <div class="controlformulario">
                    <label for="problema">Problema detectado</label>
                    <textarea name="problema" id="problema"><?= $fila['problema'] ?></textarea>
                </div>

                <div class="controlformulario">
                    <label for="fecha">Fecha de entrada</label>
                    <input type="text" name="fecha" id="fecha" value="<?= $fila['fecha'] ?>">
                </div>

                <input type="submit" name="actualizar" value="Actualizar incidencia">

            </form>

            <?php
        }
    }

} else {

    // ===============================
    // LEER INCIDENCIAS
    // ===============================

    echo "<h1>Listado de incidencias</h1>";

    echo "<table>";
    echo "<tr>";
    echo "<th>Cliente</th>";
    echo "<th>Equipo</th>";
    echo "<th>Problema</th>";
    echo "<th>Fecha</th>";
    echo "<th>Editar</th>";
    echo "<th>Eliminar</th>";
    echo "</tr>";

    $sql = "SELECT * FROM incidencias;";
    $resultado = $conexion->query($sql);

    while ($fila = $resultado->fetch_assoc()) {

        echo "<tr>";
        echo "<td>".$fila['cliente']."</td>";
        echo "<td>".$fila['equipo']."</td>";
        echo "<td>".$fila['problema']."</td>";
        echo "<td>".$fila['fecha']."</td>";
        echo "<td><a class='editar' href='?accion=editar&id=".$fila['id']."'>✎</a></td>";
        echo "<td><a class='eliminar' href='?accion=eliminar&id=".$fila['id']."'>x</a></td>";
        echo "</tr>";

    }

    echo "</table>";

    echo "<a href='?accion=nuevo' id='nuevo'>+</a>";
}

$conexion->close();

?>

</main>

</body>
</html>