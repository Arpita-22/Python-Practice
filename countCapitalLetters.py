# prints the ascii value of a alphabet
print(ord("Z"))
___________________________________________________________________________________________________________________

with open(SOME_LARGE_FILE) as fh:

text = fh.read()
_______________________________________________________________________________________________________________________
#work even on files that won't fit into memory, so we can't just read the whole file into a string.
#iter(function to call repeatedly, value that tells us when to stop also called the sentinel)
for line in iter(fh.readline(),''):
    for character in line:
        logic
_________________________________________________________________________________________________________________________
#for python 2.7 there is a method called xreadlines() wecan use instead of iter()
for line in fh.xreadlines():

#for Python3 it has inbuilt iterator for iterating over the lines .
for line in fh:

_________________________________________________________________________________________________________________________________
#counts the number of capital letters  for a text

text = "Hello World"
count = 0

for letter in text:
    # if character.isupper():
    
    if ord(letter) >= 65 and ord(letter) <= 90:
        count += 1
_______________________________________________________________________________________________________________________________
    count +=(1 if character.isupper() else 0)

    count += (1 if ord(letter) >= 65 and ord(letter) <= 90 else 0)

    count = sum(1 for line in fh for character in line if character.isupper())

    #we can even take advantage of the fact that Python will coerce True to 1 (and False to 0):
    count = sum(character.isUpper() for line in fh for character in line)
__________________________________________________________________________________________________________________________________________
# count = sum(character.isupper() for character in text)

print(count)