<?php

$incidencia = [];

$incidencia['cliente'] = "Gustavo";
$incidencia['problema'] = "No puede acceder al sistema";
$incidencia['prioridad'] = "Alta";

$json = json_encode($incidencia);

echo $json;

?>