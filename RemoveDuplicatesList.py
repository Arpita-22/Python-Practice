nos = [1, 2, 3, 4, 3, 2, 1]

#creating a dictionary from making the list items as key
myDict = dict.fromkeys(nos)

#creatind a list from myDict
myDict = list(myDict)

print(myDict) 

def removeDuplicates(nos):
    return list(dict.fromkeys(nos))

print(removeDuplicates(nos))