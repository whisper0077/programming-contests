n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    d = c
    for j in range(m):
        d += a[j] * b[j]
    if d > 0:
        ans += 1

print(ans)