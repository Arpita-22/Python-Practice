import re

text =  'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

mydict = {}


for line in text:
    print(line)
    if line.isalpha():
        wordL = line.lower()

        if wordL in mydict:
            mydict[wordL] += 1
        
        else:
            mydict[wordL] = 1

    # for word in line:
        
    #     if word.isalpha():  
    #         wordL = word.lower()
    #         print(wordL)

    #         if wordL in mydict:
    #             mydict[wordL] += 1
        
    #         else:
    #             mydict[wordL] = 1

print(mydict)