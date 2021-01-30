N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
cd = [list(map(int, input().split())) for _ in range(K)]
ans = 0
for i in range(2**K):
    p = [0]*(N+1)
    for j in range(K):
        c, d = cd[j]
        if (1 << j) & i > 0:
            p[c] += 1
        else:
            p[d] += 1

    t = 0
    for a, b in ab:
        if p[a] > 0 and p[b] > 0:
            t += 1
    ans = max(ans, t)
print(ans)
