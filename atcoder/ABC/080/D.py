T = 10**5+1
N, C = map(int, input().split())
h = [[] for _ in range(C)]
for i in range(N):
    s, t, c = map(int, input().split())
    s -= 1
    t -= 1
    c -= 1
    h[c].append([s, t])

v = [0]*T
for i in range(C):
    if len(h[i]) == 0:
        continue
    h[i].sort()
    c = h[i]
    if len(c) > 0:
        f = []
        f.append(c[0])
        for j in range(1, len(c)):
            if f[-1][1] != c[j][0]:
                f.append(c[j])
            else:
                f[-1] = [f[-1][0], c[j][1]]
        for s, t in f:
            v[s] += 1
            v[t+1] -= 1

ans = 0
use = 0
for i in range(T):
    use += v[i]
    ans = max(ans, use)
print(ans)
