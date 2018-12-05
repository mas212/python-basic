produk = "buku"
qty = 5
harga = 10000

#promo = input("anda apakah memeliki diskon? ")

if qty < 4:
	diskon = qty * harga - 1000
	if diskon > harga:
		print('--------------------------')
		print('produk = ', produk)
		print('diskon = ', diskon)
		print('--------------------------')
		print('total = ', qty * harga - diskon)
	else:
		print('--------------------------')
		print('produk = ', produk)
		print('--------------------------')
		print('total = ', qty * harga)
else:
	print('--------------------------')
	print('produk = ', produk)
	print('--------------------------')
	print('total = ', qty * harga)