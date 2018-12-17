#set, himpunan
# superhero = {
# 	"wiro sable",
# 	"cak pendekar"
# }

superhero = set()

superhero.add("mas wiro")
superhero.add("abang")
superhero.add("jos")
print(sorted(superhero))

ganjil = {1,3,5,7,9}
genap = {2, 4, 6, 8, 10}
prima = {2,3,5,7}

gabungan = ganjil.union(genap)
print(gabungan)