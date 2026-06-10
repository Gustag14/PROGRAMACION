<?php

$archivo = fopen("registro.txt", "r");

$contenido = fread($archivo, filesize("registro.txt"));

echo $contenido;

fclose($archivo);

?>