def triangle(n):
    for i in range(n):
        # line = str((i) * symbol)
        line =  " " * ((n - i) - 1) + "*" * ((2 * i) + 1)
        print(line)


triangle(9)