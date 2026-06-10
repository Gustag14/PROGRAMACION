<?php

$usuario = [
    "nombre" => "Gustavo",
    "apellidos" => "Gomez",
    "email" => "gustavo@email.com"
];

foreach($usuario as $campo => $dato){
    echo "<label>".$campo."</label>";
    echo "<input type='text' value='".$dato."'>";
    echo "<br>";
}

?>