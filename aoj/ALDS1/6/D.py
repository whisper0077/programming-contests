# Minimum cost sort

n = int(input())
*w, = map(int, input().split())
s = list(sorted(w))

si = [0] * 10001
for i, v in enumerate(s):
    si[v] = i

ans = 0
b = [False] * n
for i in range(n):
    if b[i]:
        continue
    j = i
    mw = w[i]
    z = 0
    nn = 0
    while b[j] == False:
        b[j] = True
        nn += 1
        mw = min(w[j], mw)
        z += w[j]
        j = si[w[j]]
    c = min((nn - 2) * mw + z, mw + z + (nn + 1) * s[0])
    ans += c

print(ans)