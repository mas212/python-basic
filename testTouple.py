import sys

data_list = [1, 2, 3, 4, 5, "beras", "es jus", 3.14]
data_touple = (1, 2, 3, 4, 5, "beras", "es jus", 3.14)

besar_data_list = sys.getsizeof(data_list)
besar_data_touple = sys.getsizeof(data_touple)

print(besar_data_list)
print(besar_data_touple)