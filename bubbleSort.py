myList = [32,5,3,6,7,54,87]

def bubbleSort(myList):
    n = len(myList)
    temp = 0

    for i in range(n - 1):
        swap = False
        for j in range(1, n):     
            if myList[i] > myList[j] and i < j:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
                swap = True
        
        if swap == False:
            break

        print(myList)


    return myList

print(bubbleSort(myList))
