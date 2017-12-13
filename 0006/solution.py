N = 100

A = sum([(x+1)*(x+1) for x in range(N)])
B = sum([x+1 for x in range(N)])

C = B*B - A
print(C)