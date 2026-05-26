# LIST -> SET
data_list = [1, 2, 2, 3, 4, 4, 5]
print("List sebelum:", data_list)

hasil_set = set(data_list)
print("Set sesudah:", hasil_set)


# SET -> LIST
data_set = {10, 20, 30, 40}
print("\nSet sebelum:", data_set)

hasil_list = list(data_set)
print("List sesudah:", hasil_list)



# TUPLE -> SET
data_tuple = (7, 8, 8, 9, 10)
print("\nTuple sebelum:", data_tuple)

hasil_set2 = set(data_tuple)
print("Set sesudah:", hasil_set2)

# SET -> TUPLE
data_set2 = {100, 200, 300}
print("\nSet sebelum:", data_set2)

hasil_tuple = tuple(data_set2)
print("Tuple sesudah:", hasil_tuple)