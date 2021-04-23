#using string slicing
number = 123
rev = str(123)[::-1]

revNum = int(rev)

print(revNum)

#using while loop

inputNum = 567
reverse = 0

while inputNum != 0:
    reverse = reverse * 10 + inputNum % 10
    inputNum = int(inputNum / 10)

print(reverse)
