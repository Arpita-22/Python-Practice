import re

string = 'Hello! I am Robot. This is a Python example.' 

#splits the string to each word by spaces
# string.split()
# print(string.split())

#used regex to remove any whitespaces from string

# word = "".join(re.findall("[a-zA-Z]+",string))

# word2 = (re.findall("[A-Z][^A-Z]*", word))

pat = re.compile(r'[^a-zA-Z ]+')
string = re.sub(pat, '', string).lower()

print(string)
