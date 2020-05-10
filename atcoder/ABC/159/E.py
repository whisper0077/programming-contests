H, W, K = map(int, input().split())
m = []
for h in range(H):
    m.append(list(map(int, list(input()))))

ans = float('inf')
for hb in range(2**(H-1)):
    hl = []
    for i in range(H-1):
        if hb & (1 << i) > 0:
            hl.append(i+1)
    t = len(hl)
    hl = [0]+hl+[H]

    w, pw = 0, 0
    wl = [0]*len(hl)
    while w < W:
        ok = True
        for i in range(len(hl)-1):
            sh, eh = hl[i], hl[i+1]
            for h in range(sh, eh):
                wl[i] += m[h][w]
                if wl[i] > K:
                    ok = False
                    break
            if not ok:
                break

        if not ok:
            if pw == w:
                t = float('inf')
                break
            pw, w = w, w
            t += 1
            wl = [0]*len(hl)
        else:
            w += 1

    ans = min(t, ans)

print(ans)
