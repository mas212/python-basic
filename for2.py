#list sebagai interable
produk = ["petani", "pupuk", "alat-alat", "bahan"]

for item in produk:
	print(item)
	print(len(item))

#string sebagai interable

petani = "padi"

for a in petani:
	print(a)

#for di dalam for

buah = ['semanka', 'mangga', 'melon']
sayur = ['bawang merah', "sawi", "wortel"]

daftar_belanja = [produk, buah, sayur]
print(daftar_belanja)

for subDaftarBelanja in daftar_belanja:
	for komponen in subDaftarBelanja:
		print(komponen)


cart = ["produk", "1000", "10%"]
komisi = "10"
jumlahKomisi = [cart, komisi]

for jumlah in jumlahKomisi:
	for x in jumlah:
		print(x) 