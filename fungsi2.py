#mendefiniskan fungsi
def suaraAyam():
	print("kukuruyuk!!!!")


def hargaTotalAyam(kg, harga):
	suaraAyam()
	#harga = 2000
	hargaTotalAyam = kg * harga
	print("harga ayam per potong", hargaTotalAyam)
hargaTotalAyam(4, 1000)

def addToCart(qty, price):
	subTotal = qty * price
	print("subtotal adalah", subTotal)

def total(balance):
	addToCart(2, 5000)
	total = balance + 100
	print("total", total)
total(10)
#addToCart(2, 5000)
