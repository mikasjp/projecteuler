def isPalindrome(n):
    return str(n)==(str(n))[::-1]

palindromes = []

for j in range(999, 100, -1):
    for i in range(999, 100, -1):
        N = i*j
        if isPalindrome(N):
            palindromes.append(N)

print(max(palindromes))