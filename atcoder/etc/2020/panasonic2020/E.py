a = input()
b = input()
c = input()
la, lb, lc = len(a), len(b), len(c)

M = 4000
M2 = 20000
M2offset = 10000


def canInserts(n, m, l, o):
    '''
    これすごい
    n[i]とm[j]が一致するように差し込めるindexがTrueになる
    '''
    r = [True]*l
    for i in range(len(n)):
        for j in range(len(m)):
            if n[i] != m[j] and n[i] != '?' and m[j] != '?':
                r[i-j+o] = False
    return r


ab = canInserts(a, b, M2, M2offset)
ac = canInserts(a, c, M2, M2offset)
bc = canInserts(b, c, M2, M2offset)

ans = M2
for bi in range(-M, M+1):
    if not ab[bi+M2offset]:
        continue
    for ci in range(-M, M+1):
        if ac[ci+M2offset] and bc[ci-bi+M2offset]:
            l = min(0, bi, ci)
            r = max(la, bi+lb, ci+lc)
            t = r-l
            if ans > t:
                ans = t
print(ans)
