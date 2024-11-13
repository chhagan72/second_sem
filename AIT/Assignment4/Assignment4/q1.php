
<?php

// $emp = array("Name"=>"Chhagan",
//         "Salary"=> 50000);
// $emp1 = array("Name"=>"Rejoy",
//         "Salary"=> 45000);
// $emp2 = array("Name"=>"Raj",
//         "Salary"=> 40000);
//         echo "The Salary of ".$emp["Name"]. "is Rs ".$emp['Salary']."\n";
//         echo "The Salary of ".$emp1["Name"]. "is Rs ".$emp['Salary']."\n";
//         echo "The Salary of ".$emp2["Name"]. "is Rs ".$emp['Salary']."\n"
?>

<?php    
/* First method to create an associate array. */
$student_one = array("Chhagan"=>95000, "Rejoy"=>90000,   
                  "Raj"=>70000);  
    
/* Second method to create an associate array. */
$student_two["Maths"] = 95;  
$student_two["Physics"] = 90;  
$student_two["Chemistry"] = 96;  
$student_two["English"] = 93;  
$student_two["Computer"] = 98;  
    
/* Accessing the elements directly */
echo "Marks for student one is:\n";  
echo "Maths:" . $student_two["Maths"], "\n";  
echo "Physics:" . $student_two["Physics"], "\n";  
echo "Chemistry:" . $student_two["Chemistry"], "\n";  
echo "English:" . $student_one["English"], "\n";  
echo "Computer:" . $student_one["Computer"], "\n";  
?>