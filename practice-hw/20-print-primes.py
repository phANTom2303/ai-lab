def isPrime(num):
    if(num <= 1):
        return False 
    
    if(num == 2):
        return True
    
    for i in range(2, num//2 + 1):
        if(num % i == 0):
            return False 
    return True

for i in range(1,51):
    if(isPrime(i)):
        print(i)