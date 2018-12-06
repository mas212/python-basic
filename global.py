name = "hariyanto"

def person():
	print("nama anda " + name)

person()

#global variabel

product ={
	'name' : 'pupuk',
	'harga' : '50000',
	'item' : '10',
	'point' : '9'
}

def cart():
	global product
	if product['name'] > product['harga']:
		print('dapat point --> ' + product['point'])
	else:
		print('beli lagi')

	discount = {
		'discount' : '10%'
	}

	#local variabel
	print(discount['discount'])

cart()

#global variabel call
print(product['name'], product['harga']) 

