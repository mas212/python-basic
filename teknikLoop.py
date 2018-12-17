nama_band = [
	"payung teduh",
	"fourtwy",
	"dialog di pagi hari",
	"efek rumah kaca"
]

kumpulan_lagu = [
	"akad",
	"zona nyaman",
	"rumahku",
	"dang filsuf"
]

for i, band in enumerate(nama_band):
	print("no ", i , "nama band", band)

#pegabungan --->zip

for band, lagu in zip(nama_band, kumpulan_lagu):
	print(band, " judul lagu sebagai berikut ->", lagu)


playlist = {"akad", "cinta", "jaran goyang", "pupus", "mantab"}

for list in sorted(playlist):
	print(list)

playlist2 = {
	"name" : "mas",
	"position" : "backend developer",
	"status" : "staff remote"
}

for position, val in playlist2.items():
	print(position, ">>", val)