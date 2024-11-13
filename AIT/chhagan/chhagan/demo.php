<?php
echo "\n This si a good programming language";

function myfunc()
{
    echo"\nThis is a with out argument";
}

function myfunc2($name)
{
    echo"\nThis is a with arguements ",$name;

}
myfunc2("chhagan");
function myfunc3($name)
{
    return $name;
    // echo" This is a with arguements";

}
echo myfunc3("chhagan");



?>