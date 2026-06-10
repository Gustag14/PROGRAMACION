<?php

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

try {

    $json = file_get_contents('php://input');

    if ($json === false || trim($json) === '') {
        throw new RuntimeException('No se han recibido datos');
    }

    $pedido = json_decode($json, true, 512, JSON_THROW_ON_ERROR);

    $pedido['_created_at'] = new MongoDB\BSON\UTCDateTime((int)(microtime(true) * 1000));

    $manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

    $bulk = new MongoDB\Driver\BulkWrite();

    $id = $bulk->insert($pedido);

    $manager->executeBulkWrite('cafeteria.pedidos', $bulk);

    echo json_encode([
        'ok' => true,
        'id' => (string)$id
    ], JSON_UNESCAPED_UNICODE);

} catch (Throwable $e) {

    http_response_code(500);

    echo json_encode([
        'ok' => false,
        'error' => $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);

}

?>