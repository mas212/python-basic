buah = ["semangka", "mangga", "salak"]

for macam in buah:
	print(macam)

for nilai in range(4):
	print(nilai)


total = 0

for subtotal in range(1, 100):
	if subtotal % 3 == 0:
		total += subtotal
print(total)

items = 1

for product in range(1, 10):
	if product % 2 == 0:
		items += product
print(items)


itemsList = {
	"data" : "category-product",
	"subcategory": {
		"name" :  "fashion"
	}
}


for key, value in itemsList.items():
	print(key, value)
