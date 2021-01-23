N, X = map(int, input().split())
ans = -1
a = 0
for i in range(N):
    v, p = map(int, input().split())
    a += v*p
    if a > X*100:
        ans = i+1
        break
print(ans)
