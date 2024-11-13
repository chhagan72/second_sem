<?php
$servername = "localhost";
$username ="root";
$password ="";
$dbname  ="student";
$conn = new mysqli($servername,$username,$password,$dbname);
if($conn ->connect_error){
    die("Connection failed:".$conn->connect_error);
}
?>


<!-- CREATE TABLE std_info ( id int, LastName varchar(20), FirstName varchar(20), Address varchar(20), mobile int(11) );? -->