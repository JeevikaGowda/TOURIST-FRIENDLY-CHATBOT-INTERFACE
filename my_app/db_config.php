<?php
// Database configuration
$host = "localhost"; // Hostname
$username = "root"; // Database username
$password = "2684"; // Database password
$database = "tourlydb"; // Database name

// Create connection
if (!function_exists('mysqli_init') && !extension_loaded('mysqli')) {
    echo 'We don\'t have mysqli!!!';
} else {
    echo 'Phew we have it!';
}

$mysqli = new MySQLi($host, $username, $password, $database);

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}
?>
