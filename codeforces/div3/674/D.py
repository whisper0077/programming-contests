n = int(input())
*a, = map(int, input().split())
h = {0: 1}
s = 0
ans = 0
for i in range(n):
    s += a[i]
    if s in h:
        ans += 1
        s = a[i]
        h = {0: 1}
    h[s] = i
print(ans)
