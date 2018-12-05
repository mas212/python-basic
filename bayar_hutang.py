uang = input("kamu punya uang berapa? ")
utang = 1000

if int(uang) < utang:
	print("gak cukup bos")
elif int(uang) == utang:
	print("terima kasih sudah bayar kak")
else:
	print("uang anda masih sisa banyak")