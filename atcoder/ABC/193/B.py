N = int(input())
d = 0
la = 0
ans = 10**10
for i in range(N):
    a, p, x = map(int, input().split())
    d += (a-la)
    x -= d
    la = a
    if x > 0:
        ans = min(ans, p)
if ans == 10**10:
    ans = -1
print(ans)
