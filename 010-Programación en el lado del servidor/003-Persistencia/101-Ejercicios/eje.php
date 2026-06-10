<?php

$archivo = fopen("registro.txt", "a");

fwrite($archivo, "Nueva incidencia registrada\n");

fclose($archivo);

?>