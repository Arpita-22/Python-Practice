import random

myList = ['abb','baa','c','d']

# print(myList)
x = 1.5
x = float(1.5) # typecasting
print(x)
x = "A"
print(x)


#assign values to multiple variables and the no of values should match the no of variables
x, y, z = "apple", "grapes", "orange"
print(x,y,z)

#assign one value to multiple variables

a = b = c = "hello"
print(a,b,c)

#unpacking a collection
nos = [1,2,3]
# a = b = c = nos
# print(a, b, c)
e ,f ,g = nos
print(e,f,g)

#output variables
var = "world"
print("hello" + " " +var)

#global variables
x = "apple"
def myFunc():
    #if you comment out the local variable x the function would print the global variable
    x = "orange"
    print(x)
myFunc()
print(x)

#using global scope
x = "bad"
def myFunc():
    #to change the value of a global variable
    global x
    x = "good"

myFunc()
print(x)

#complex no
z = 1j
print(type(z))

#random number
print(random.randrange(1,10))

#multiline string
a = ''' H
    R '''

b = """ W
    O """

print(a + b)

#loop

text = "hello"

for x in text:
    print(x)

#if condition and find

print("o" in text)

if "e" in text:
    print("present")

#if not  and not condition

print("w" not in text)

if "w" not in text:
    print("not present")

"""format() method can combine strings and numbers, it takes unlimited arguments are placed into respective placeholders,
Index nos can be used to be sure that the arguments are placed in the right order
"""
ageNow = 36
ageBefore = 17
# txt = "I was {} before, now I am {} years old"
# print(txt.format(ageBefore, ageNow))
txt = "I was {1} before, now I am {0} years old"
print(txt.format(ageNow, ageBefore))


