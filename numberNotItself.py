big_num_1 = 1000
big_num_2 = 1000
small_num_1 = 1
small_num_2 = 1

#keyword is tests whether the two objects are same not just equals
print(big_num_1 is big_num_2)
print(small_num_1 is small_num_2)

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print("list_1 == list_2? %s" % (list_1 == list_2))
print("list_1 is list_2? %s" % (list_1 is list_2))

# for num in range (1001):
for num in range (-1001, 0):
    num_copy = num * 1
    if num_copy is num:
        print(num, "singleton")
    else:
        print( num, "not singleton")

# numbers from -5 to 256 have singleton instances so they return true when tested with is