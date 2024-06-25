<?php
require_once 'db_config.php';

try {
    $mysqli->query("USE tourlydb");
    echo "Connected successfully to the database.";
} catch (Exception $e) {
    echo "Error connecting to the database: " . $e->getMessage();
}
?>