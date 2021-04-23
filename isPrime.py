def prime(n):
    num = n
    isPrime = True

    for i in range(2, n):
        if num % i == 0:
            isPrime = False
            break
    
    if isPrime == True:
        print("prime number")

    else:
        print("not a prime number")


prime(112)

