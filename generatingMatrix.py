matrix = [[(j * i) for j in range (1, 4)] for i in range(1, 4)]

# for i in range(1, 4):
#     for j in range(1, 4):
#         matrix.append(j * i)

# iterator = (i for i in range(1, 4))
iterator = [i for i in range(1, 4)]
matrix = [[x * y for y in iterator] for x in iterator]

print(matrix)
