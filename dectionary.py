_data_produk = {
	'nama' 	: 'buah semangka',
	'qty' 	: 10,
	'stock' : '20',
	'harga' : {
		'diskon' : 25000,
		'normal' : 30000
	}
}

# for key, value in _data_produk.items():
# 	print(key + " = " + value)

# if _data_produk["harga"] > "1000":
# 	for key, value in _data_produk.items():
# 		print(key + " = " + value)
# else:
# 	print("hasil data salah")
total = _data_produk["harga"]['normal'] - _data_produk['harga']['diskon']  
normal = _data_produk["harga"]['normal'] * _data_produk["qty"] 
if total > 10000:
	print("anda dapat diskon")
else:
	print("data total produk = ", normal)