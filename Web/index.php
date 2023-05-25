<?php 
require 'baglan.php'
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Sipariş Al</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="order">
		<div class="order-screen">
			<div class="app-title">
				<h1>Sipariş Oluştur</h1>
			</div>
			<form action="islem.php" method="post">
			<div class="order-form">
				<div style="color: crimson; font-size: 15px; margin-bottom: 10px;">* Doldurulması zorunlu alan</div>
				
				<div class="control-group">
					<input type="text" name="customername" class="order-field" placeholder="* İşletme İsmi" id="order-name">
					<label class="order-field-icon fui-user" for="order-name"></label>
				</div>
				<div class="control-group">
					<input type="text" name="telno" class="order-field" placeholder="* Tel. No (Boşluk Olmadan)">
					<label class="order-field-icon fui-user" for="order-num"></label>
				</div>
				<div class="control-group">
					<input type="email" name="email" class="order-field" placeholder="* E-posta">
					<label class="order-field-icon fui-user" for="order-mail"></label>
				</div>
				<div class="control-group">
					<input type="text" name="siparis" class="order-field" placeholder="* Siparişinizi açıklayınız">
					<label class="order-field-icon fui-user" for="order-place"></label>
				</div>

				<button href="index.php" class="btn btn-primary btn-large btn-block" name="olustur">Siparişi Gönder</button>
			</div>
			</form>
		</div>
	</div>

</body>
</html>