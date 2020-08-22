H, W, M = map(int, input().split())
r = [0]*(W+1)
c = [0]*(H+1)
rc = {}
for i in range(M):
    h, w = map(int, input().split())
    rc[(h, w)] = True
    r[w] += 1
    c[h] += 1

rm = max(r)
cm = max(c)

ri = {i for i, v in enumerate(r) if v == rm}
ci = {i for i, v in enumerate(c) if v == cm}

cnt = sum([w in ri and h in ci for h, w in rc])
print(rm+cm-(len(ri)*len(ci) == cnt))
