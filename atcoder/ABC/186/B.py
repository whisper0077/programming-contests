H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
m = 10**9
for h in range(H):
    m = min(m, min(A[h]))
ans = 0
for h in range(H):
    for w in range(W):
        ans += A[h][w]-m
print(ans)
