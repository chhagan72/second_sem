<?php

if (isset($_POST['u_name']) && isset($_POST['u_age']) && isset($_POST['u_email'])) :

    $db_conn = mysqli_connect("localhost", "root", "", "my_test_db");

    $name = $_POST['u_name'];
    $age = $_POST['u_age'];
    $email = $_POST['u_email'];

    $sql = "INSERT INTO `users` (`name`, `age`, `email`) VALUES ('$name', $age, '$email')";

    $query = mysqli_query($db_conn, $sql);

    if ($query) {
        echo 'New data inserted successfully. <a href="./index.html">Go Back</a>';
    } else {
        echo "Failed to insert new data.";
    }
    exit;
endif;

echo '404 Page Not Found. <a href="./index.html">Go Home</a>';