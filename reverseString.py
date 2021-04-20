text = "name"

#Using slicing no start or end string is given, -1 here means it would start from the reverse order
reverse = text[:: -1]
print(reverse)

#using for loop
rev = ""
for character in text:
    rev = character + rev  
print(rev)

#using while loop
revStr = ""
length = len(text) - 1

while length >= 0:
    revStr += text[length]
    length -= 1
print (revStr)

#using list.reverse()
txt = list(text)
txt.reverse()
revS = "".join(txt)

print(revS)
