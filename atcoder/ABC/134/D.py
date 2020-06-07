def divisor(n):
    # nの約数列挙
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない


N = int(input())
*a, = map(int, input().split())
a = [0]+a
b = []
c = [0]*(N+1)

for i in range(N, 0, -1):
    if c[i] % 2 != a[i]:
        b.append(i)
        for d in divisor(i):
            if i % d == 0:
                c[d] += 1

print(len(b))
if len(b) > 0:
    print(*b)
