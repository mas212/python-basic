class Catalog:

	__price = 500

	def __init__(self, product_name, product_qty, product_price, product_description):
		self.product = product_name
		self.qty = product_qty
		self.price = product_price
		self.description = product_description

	def  getProductItem(self):
		print(self.product, self.qty, self.price, self.description)

	def getStock(self):
		if self.qty <= 2:
			print("stock habis gan", self.qty)
		else:
			print("stock banyak gan")

	def getPriceDiskon(self, price):
		self.__price = price

	def checkPrice(self):
		if self.__price <= 500:
			print("belum waktu nya gan")
		else:
			print("diskon cuy")

	def cart(self, qty, price):
		total = self.qty * self.price
		return total

item = Catalog("pupuk", 10, 1000, "oke bos")
item.getProductItem()
item.getStock()

#akses private method
item.getPriceDiskon(1000)
item.checkPrice()

print(item.cart(10, 2000))