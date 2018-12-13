angka = 0

while angka < 5:
	print("oke while di dalam", angka)
	angka += 1
print("di luar while")

start = True
angka = 0

while start:
	print("boolean while")
	if angka is 100:
		start = False
		print("menemukan 100")
	angka += 1
print("di luar while boolean")