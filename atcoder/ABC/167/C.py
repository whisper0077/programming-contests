N, M, X = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
for i in range(2**N):
    tca = [0]*(M+1)
    for j in range(N):
        if i & (1 << j) > 0:
            for k in range(M+1):
                tca[k] += ca[j][k]
    if min(tca[1:]) >= X:
        ans = min(ans, tca[0])

if ans != float('inf'):
    print(ans)
else:
    print(-1)
