<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro de incidencia</title>

    <style>
        html, body {
            width: 100%;
            height: 100%;
            padding: 0;
            margin: 0;
        }

        body {
            display: flex;
            align-items: center;
            justify-content: center;
            background: #e8e8e8;
            flex-direction: column;
            font-family: Arial, sans-serif;
        }

        header, main, footer {
            width: 420px;
            padding: 20px;
            background: white;
            text-align: center;
            margin: 5px;
            border-radius: 8px;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        input, textarea {
            padding: 10px;
        }

        textarea {
            resize: none;
            height: 80px;
        }
    </style>
</head>

<body>

<header>
    <h1>Soporte técnico</h1>
</header>

<main>
    <form action="?" method="POST">

        <label for="cliente">Nombre del cliente</label>
        <input type="text" name="cliente" id="cliente">

        <label for="problema">Problema detectado</label>
        <textarea name="problema" id="problema"></textarea>

        <input type="submit" value="Guardar incidencia">

    </form>
</main>

<footer>

<?php

if(isset($_POST['cliente']) && isset($_POST['problema'])){

    $json = json_encode($_POST);

    $archivo = fopen(date('U').".json", "w");

    fwrite($archivo, $json);

    fclose($archivo);

    echo "Incidencia guardada correctamente";
    echo "<br>";
    echo $json;

}

?>

</footer>

</body>
</html>