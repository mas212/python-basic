def argument(nilai):
	a = nilai**2
	print("ini",a)
	return a

def tambah(argumen1, argumen2):
	total = argumen1 + argumen2
	print("total tambah", total)
	return total
b = argument(10)
print(b)

totalSemua = tambah(10,20)
print(totalSemua * tambah(10, 20))