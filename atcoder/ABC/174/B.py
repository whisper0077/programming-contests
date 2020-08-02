N, D = map(int, input().split())
ans = 0
D2 = D*D
for i in range(N):
    x, y = map(int, input().split())
    if (x*x+y*y) <= D2:
        ans += 1

print(ans)
