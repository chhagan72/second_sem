<?php
include "p1.php";

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Document</title>
</head>

<body>
    <div class="form1">

        <h2>Student Form</h2>
        <form action="#" method="POST">
            <label for="#">Id:</label><br>
            <input type="text" name="id" id="id"><br>

            <label for="#">FirstName:</label><br>
            <input type="text" name="fname" id="fname"><br>

            <label for="#">LastName:</label><br>
            <input type="text" name="lname" id="lname"><br>

            <label for="#">Address:</label><br>
            <input type="text" name="address" id="address"><br>

            <label for="#">Mobile:</label><br>
            <input type="text" name="mobile" id="mobile"><br>

            <input type="submit" name="submit" id="submit" value="Submit"><br>
        </form>
    </div>
</body>

</html>

<?php
include "p1.php";
    if(isset($_POST['submit']))
    {
        $id = $_POST["id"];
        $fname = $_POST["fname"];
        $lname = $_POST["lname"];
        $add = $_POST["address"];
        $mobile = $_POST["mobile"];
        $sql = "INSERT INTO 'std_info'('Fname','Lname','Address','mobile') VALUES('$fname','$lname','$add','$mobile')";
        $result = $conn->query($sql);
        if($result == TRUE)
        {
            echo" New record is created successfully";
            header('Location:view.php');
        }
        else{
            echo" Error:".$sql."<br>".$conn->error;
            
        }
        $conn->close();

}
?>