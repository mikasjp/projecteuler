fib = [0, 1]



while fib[-1]<4000000:
    fib.append(fib[-1]+fib[-2])

fib.pop()

ans = sum([x for x in fib if x%2==0])

print(ans)