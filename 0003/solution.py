import math

N = 600851475143

def isPrime(n):
    prime = True
    for i in range(2, n-1):
        if n%i==0:
            prime = False
            break
    return prime

for i in range(int(math.sqrt(N)), 1, -1):
    if N%i==0:
        if isPrime(i):
            print(i)
            break