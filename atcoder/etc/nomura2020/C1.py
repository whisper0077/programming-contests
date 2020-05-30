N = int(input())
*A, = map(int, input().split())

Pmax = [0 for _ in range(N+1)]
Pmax[0] = 1-A[0]
for i in range(1, N+1):
    Pmax[i] = 2*Pmax[i-1] - A[i]

ans = 0
v = 0
for i in range(N, -1, -1):
    if Pmax[i]*2 < v:
        ans = -1
        break
    v = min(v, Pmax[i])+A[i]
    ans += v

print(ans)
