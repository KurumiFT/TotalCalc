<?php
$calc = file_get_contents("https://raw.githubusercontent.com/OntoTube/TotalCalc/master/calc.py");
$file = fopen("calc.py", "w");
fwrite($file, $calc);
fclose($file); 
?>
