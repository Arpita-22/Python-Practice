string = 'abcdefghghghghghgh.'
substring = 'ghg'
count = 0
index = 0
# s = string.find("aba", index)

for i in range(len(string)):
    if substring in string:
        count += 1
    string = string[i+1 : ]

print(count)

