import itertools
N, K = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(N)]

ans = 0
p = [i for i in range(1, N)]
for v in itertools.permutations(p, N-1):
    c = t[0][v[0]]
    for i in range(len(v)-1):
        c += t[v[i]][v[i+1]]
    c += t[v[N-2]][0]
    if c == K:
        ans += 1

print(ans)
