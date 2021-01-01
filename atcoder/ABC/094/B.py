n, m, x = map(int, input().split())
*a, = map(int, input().split())
ans = 0
for i in range(m):
    if a[i] > x:
        ans = min(ans+i, ans+m-i)
        break
print(ans)
