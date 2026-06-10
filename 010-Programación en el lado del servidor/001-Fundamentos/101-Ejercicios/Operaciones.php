<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Cartelera</title>

    <style>
        .dia{
            border:1px solid black;
            padding:10px;
            width:50px;
            height:50px;
            display:inline-block;
            text-align:center;
            margin:3px;
        }
    </style>
</head>

<body>

<h1>Calendario de cartelera</h1>

<?php

for($dia = 1; $dia <= 30; $dia++){
    echo "<div class='dia'>".$dia."</div>";
}

?>

</body>
</html>