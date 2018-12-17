class Mahasiswa():

	nama = 'nama'
	def __init__(self,input_nama, input_nim):
		self.nama = input_nama
		self.nim  = input_nim


	def belajar(self, kondisi):
		print(self.nama,"saya belajar python dev method", kondisi)

	def tidur(self):
		print(self.nama, "sednag tidur")

siswa = Mahasiswa("mas", 1100021)
siswa.belajar("study hard")
print(siswa.nama)
print(siswa.nim)
