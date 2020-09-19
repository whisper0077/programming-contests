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
for i in range(n):
    if i % 2 == 0:
        b[i] = a[ai]
        ai += 1
for i in range(1, n-1):
    if i % 2 == 1:
        if b[i] < b[i-1] and b[i] < b[i+1]:
            ans += 1
print(ans)
print(*b)
