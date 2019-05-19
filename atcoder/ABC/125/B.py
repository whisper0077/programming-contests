N = int(input())
*V, = map(int, input().split())
*C, = map(int, input().split())
ans = 0
for i in range(N):
    d = V[i]-C[i]
    if d > 0:
        ans += d
print(ans)
