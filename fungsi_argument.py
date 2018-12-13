#function argument

def siswa(nama):
	print("siswa adalah", nama)

siswa("mas harry")

def guru(nama, pelajaran):
	print("guru adalah", nama)
	print("mengajar", pelajaran)

guru(nama="harry", pelajaran="python dev")

#set default argument

def penjagaSekolah(nama, shift="pagi", sifat="tidak"):
	print("nama", nama)
	print("shift", shift)
	print("sifat", sifat)
penjagaSekolah("latief")
penjagaSekolah("latief", shift="siang", sifat="sabar")

def discount(price, persent):
	discount = price / persent
	if discount < 1000:
		print("belanja anda--> ",discount)
	else:
		print("belanja lagi")
discount(1000, 2)

def transaksiPengeluaran(nama,omset, modal):
	print("nama pengeluaran", nama)
	total = omset * modal
	print("total modal", total)
transaksiPengeluaran("pendapatan harian", 2000, 200000)
