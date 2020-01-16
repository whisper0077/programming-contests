N, x = map(int, input().split())
*a, = map(int, input().split())
a = a+[0]
ans = 0
for i in range(0, N):
    d = a[i]+a[i+1]-x
    if d > 0:
        for j in range(i+1, i-1, -1):
            s = min([a[j], d])
            d -= s
            a[j] -= s
            ans += s
print(ans)
