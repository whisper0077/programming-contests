N = int(input())
A = list(map(int, input().split()))

Amax = [0]*N
Aans = [0]*N
Amax[0] = max(0, A[0])
Aans[0] = A[0]
for i in range(1, N):
    Aans[i] = Aans[i-1]+A[i]
    Amax[i] = max(Aans[i], Amax[i-1])

ans = 0
c = 0
for i in range(N):
    ans = max(c+Amax[i], ans)
    c += Aans[i]
    ans = max(c, ans)

print(ans)
