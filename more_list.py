barang = ["rokok", "es", "hamiton", "beras", "gula"]

barang.insert(2, "es")
print(barang)
jumlahBarang = barang.count('rokok')
print(jumlahBarang)
#data remove
barang.remove('es')
print(barang)

stuff = barang
stuff.append("gedang goreng")
print(stuff)