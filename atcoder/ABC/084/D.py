def isPrime(n):
    # nの素数判定
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


p = [False]*(10**5+1)
c = [0]*(10**5+1)

for i in range(2, len(p)):
    p[i] = isPrime(i)
    c[i] = c[i-1]
    if i % 2 == 1 and p[i] and p[i//2+1]:
        c[i] += 1

Q = int(input())
for q in range(Q):
    l, r = map(int, input().split())
    print(c[r]-c[l-1])
