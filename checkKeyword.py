import keyword

if __name__ == '__main__':
#user input
    s = input('Enter a string:')

#check if the string is a keyword
    isKey = keyword.iskeyword(s)

print(isKey)

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#get all keywords, tjis gives us a list and to access the individual element loop through all the elements in the list
print(keyword.kwlist)