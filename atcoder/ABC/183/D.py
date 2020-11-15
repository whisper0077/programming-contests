N, W = map(int, input().split())
d = [0]*(10**6)
for i in range(N):
    s, t, p = map(int, input().split())
    d[s] += p
    d[t] -= p

a = [0]*len(d)
a[0] = d[0]
for i in range(1, len(d)):
    a[i] += a[i-1]+d[i]

ans = "Yes"
for i in range(len(d)):
    if a[i] > W:
        ans = "No"
        break
print(ans)
