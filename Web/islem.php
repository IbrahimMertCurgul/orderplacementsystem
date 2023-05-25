<?php 

require 'baglan.php';

if(isset($_POST['olustur'])){
	$customername = $_POST['customername'];
	$telno = $_POST['telno'];
	$email = $_POST['email'];
	$siparis = $_POST['siparis'];
	$tarih = date("Y-m-d H:i:s");

	if (!$customername){
		echo "HATA! Lütfen işletmenizin ismini giriniz.";
	} elseif (!$telno) {
		echo "HATA! Lütfen telefon numaranızı giriniz.";
	} elseif ($telno == trim($telno) && strpos($telno, ' ') !== false && len($telno) > 11 ) {
    	echo 'HATA! Lütfen telefon numaranızı boşluk bulundurmayacak şekilde ve doğru giriniz.';
	} elseif (!$email) {
		echo "HATA! Lütfen e-posta adresinizi giriniz.";
	} elseif (!$siparis) {
		echo "HATA! Lütfen sipariş yazınızı giriniz.";
	} else{
		$sorgu = $db->prepare('INSERT INTO siparistablosu SET tarih = ?,isletmeismi = ?, telefon = ?, email = ?, siparis = ?');
		$ekle = $sorgu->execute([$tarih, $customername, $telno, $email, $siparis]);

		if ($ekle) {
			echo "Siparişiniz başarıyla iletildi. Sayfayı kapatabilirsiniz.";
			header('Refresh:2; index.php');
		} else{
			echo "İşlem gerçekleştirilirken bir sorun oluştu. Bu numarayı arayabilirsiniz: 05xx xxx xx xx";
		}
	}
}
?>