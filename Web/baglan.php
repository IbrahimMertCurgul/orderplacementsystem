<?php 

try {
	$db = new PDO("mysql:host=localhost; dbname=siparisvt; charset=utf8", 'root', '12345678');
	//echo "işlem başarılı";
	}
catch(Exception $e)
{
	echo $e->getMessage();
}

?>