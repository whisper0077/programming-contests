n = int(input())
*a, = map(int, input().split())
a.sort()
b = [0]*n
ai = 0
ans = 0
for i in range(n):
    if i % 2 == 1:
        b[i] = a[ai]
        ai += 1
        if i < n-1:
            ans += 1
for i in range(n):
    if i % 2 == 0:
        b[i] = a[ai]
        ai += 1
print(ans)
print(*b)
