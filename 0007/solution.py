primes = []

def isPrime(n):
    prime = True
    for i in range(2, n-1):
        if n%i==0:
            prime = False
            break
    return prime

k = 1

while primes.__len__()<10002:
    if isPrime(k):
        primes.append(k)
    k += 1

print(primes[-1])