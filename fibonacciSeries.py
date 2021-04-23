#find the nth fibonacci no
def fibo(n):
    if n < 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return(fibo(n - 1) + fibo(n - 2))

print(fibo(5))

#find fibonacci series

def fiboS(n):
    fibArr = [0, 1]
    if n < 0:
        return
    if n == 1:
        return fibArr
    
    # for i in range(0,n):
    #     fibArr.append(fiboS(i))

    for i in range(2, n):
        fibArr.append(fibArr[i - 1] + fibArr[i - 2])

    return fibArr

print(fiboS(8))







