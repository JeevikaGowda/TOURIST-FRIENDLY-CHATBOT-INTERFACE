<?php
// require_once 'db_config.php';

// Define variables and initialize with empty values
$name = $age = $mobile = $email = $guests = $availability = $package = $price = '';

// Process form data when the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $age = $_POST['age'];
    $mobile = $_POST['mobile'];
    $email = $_POST['email'];
    $guests = $_POST['guests'];
    $availability = $_POST['availability'];
    $package = $_POST['package'];
    $price = $_POST['price'];
    echo "$name";
}
    // Prepare an insert statement
//     $sql = "INSERT INTO Booking (name, age, mobile, email, guests, availability, package, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
//     if ($stmt = $mysqli->prepare($sql)) {
//         // Bind variables to the prepared statement as parameters
//         $stmt->bind_param("sissssss", $param_name, $param_age, $param_mobile, $param_email, $param_guests, $param_availability, $param_package, $param_price);

//         // Set parameters
//         $param_name = $name;
//         $param_age = $age;
//         $param_mobile = $mobile;
//         $param_email = $email;
//         $param_guests = $guests;
//         $param_availability = $availability;
//         $param_package = $package;
//         $param_price = $price;

//         // Attempt to execute the prepared statement
//         if ($stmt->execute()) {
//             // Redirect to success page
//             header("Location: success.php");
//             exit();
//         } else {
//             echo "Oops! Something went wrong. Please try again later.";
//         }

//         // Close statement
//         $stmt->close();
//     }
// }

// // Close connection
// $mysqli->close();
?>