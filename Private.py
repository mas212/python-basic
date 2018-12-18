class Private():
	__nilai = 0 #private

	def __init__(self, input_nama, input_nim):
		self.nama = input_nama #public
		self.nim = input_nim #public

	def uts(self, input_nilai):
		self.__nilai = input_nilai

	def uas(self, input_nilai):
		self.__nilai = input_nilai

	def check_nilai(self):
		if self.__nilai <= 50:
			print("gagal lulus", self.nama)
		else:
			print("lulus", self.nama)

mahasiswa = Private("mas harry", 1001121)

mahasiswa.uts(50)
mahasiswa.uas(70)
mahasiswa.check_nilai()
