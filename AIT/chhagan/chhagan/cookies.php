<?php
setcookie("user","Megha", time()+1*05*05);
if(isset($_COOKIE["user"]))
{
    echo"value of cookies".$_COOKIE["user"];
}
else{
    echo "not valid cookies";
}
?>