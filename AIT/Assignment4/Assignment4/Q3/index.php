<?php
include "config.php";

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="userLogin">
        <h2>User Resistrstion</h2>
            <form action="#" method="post">
            <label for="#" name="id">Userid:</label><br>
            <input type="text"><br>
            <label for="#" name="fname">FirstName:</label><br>
            <input type="text"><br>
            <label for="#" name="lname">LastName:</label><br>
            <input type="text"><br>
            <label for="#" name="email">Email:</label><br>
            <input type="text"><br>
            <label for="#" name="mobile" >Mobile:</label><br>
            <input type="text"><br>
            <label for="#" name="password" >Password:</label><br>
            <input type="text"><br>
            <input type="submit" class="submit" value="Submit"><br>
        </form>
    </div>
</body>
</html>

<?php
include "config.php";
    // if(isset($_POST['submit']))
    if($_SERVER['REQUEST_METHOD'] === 'POST')
    {
        $username = $_POST["id"];
        $fname = $_POST["fname"];
        $lname = $_POST["lname"];
        $email = $_POST["email"];       
        $mobile = $_POST["mobile"];
        $password = $_POST["password"];
        $sql = "INSERT INTO users(id,first_name,last_name,email,mobile,password) VALUES('$username','$email','fname','lname','$mobile','$password')";
        $result = mysqli_query($conn, $sql);
        if($result)
        {
            echo" New record is created successfully";
            // header('Location:view.php');
        }
        else{
            echo" Error:". mysqli_errno($connection);
            
        }
        $conn->close();

}
?>