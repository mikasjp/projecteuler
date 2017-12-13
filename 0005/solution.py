import math

A = []

def Factorize(n):
    factors = []

    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n /= i
        if n == 1:
            break

    return factors

for i in range(2,21):
    A.append(Factorize(i))

occurences = [0 for x in range(A.__len__()+1)]

for i,q in enumerate(occurences):
    for x in A:
        if x.count(i+1)>occurences[i]:
            occurences[i] = x.count(i+1)

solution = 1

for i,x in enumerate(occurences):
    solution *= math.pow(i+1, x)

print(solution)