<?php

session_start();

$_SESSION['usuario'] = "Gustavo";
$_SESSION['plan'] = "Premium";

?>

<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>

<body>

<h1>Sesión iniciada</h1>

<a href="panel.php">
Ir al panel
</a>

</body>
</html>