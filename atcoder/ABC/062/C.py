H, W = map(int, input().split())
S = H*W
ans = 10**19
for w in range(1, W//2+1):
    s = w*H
    w2s = ((W-w)//2)*H
    h2s = (H//2)*(W-w)

    ws = [s, w2s, S-w2s-s]
    hs = [s, h2s, S-h2s-s]
    wm = max(ws)-min(ws)
    hm = max(hs)-min(hs)
    m = min(wm, hm)
    if m < ans:
        ans = m

H, W = W, H
for w in range(1, W//2+1):
    s = w*H
    w2s = ((W-w)//2)*H
    h2s = (H//2)*(W-w)

    ws = [s, w2s, S-w2s-s]
    hs = [s, h2s, S-h2s-s]
    wm = max(ws)-min(ws)
    hm = max(hs)-min(hs)
    m = min(wm, hm)
    if m < ans:
        ans = m
print(ans)
