
n = int(input())
r = [int(input()) for i in range(n)]

m = r[n-1]
ans = -10**10
for i in range(n-2, -1, -1):
    t = m-r[i]
    if t > ans:
        ans = t
    if r[i] > m:
        m = r[i]
print(ans)
