D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
ans = 10**10
for i in range(2**D):
    r = 0
    g = 0
    t = 0
    for j in range(D):
        p, c = pc[j]
        if i & (1 << j) > 0:
            t += p
            g += (j+1)*100*p+c
        else:
            r = j

    if g < G:
        p, c = pc[r]
        rg = G-g
        rp = max(1, rg//((r+1)*100))
        if rp < p:
            ans = min(ans, t+rp)
    else:
        ans = min(ans, t)
print(ans)
