<?php

session_start();

?>

<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel</title>
</head>

<body>

<h1>Panel de usuario</h1>

<?php

if(isset($_SESSION['usuario']) && isset($_SESSION['plan'])){

    echo "Usuario: ".$_SESSION['usuario'];

    echo "<br>";

    echo "Plan: ".$_SESSION['plan'];

}else{

    echo "No hay sesión iniciada";

}

?>

</body>
</html>