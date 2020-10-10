MOD = 10**9+7
H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
k = 0
for h in range(H):
    k += S[h].count('.')

if k > 0:
    wc = [[0]*W for _ in range(H)]
    for h in range(H):
        c = 0
        for w in range(W):
            c += 1
            if S[h][w] == "#":
                c = 0
            wc[h][w] = c
        for w in range(W-2, -1, -1):
            if wc[h][w] > 0 and wc[h][w] < wc[h][w+1]:
                wc[h][w] = wc[h][w+1]

    hc = [[0]*W for _ in range(H)]
    for w in range(W):
        c = 0
        for h in range(H):
            c += 1
            if S[h][w] == "#":
                c = 0
            hc[h][w] = c
        for h in range(H-2, -1, -1):
            if hc[h][w] > 0 and hc[h][w] < hc[h+1][w]:
                hc[h][w] = hc[h+1][w]

    mods = [1]*(k+1)
    for i in range(1, k+1):
        mods[i] = mods[i-1]*2 % MOD

    ans = k*mods[k] % MOD
    for h in range(H):
        for w in range(W):
            c = hc[h][w]+wc[h][w]-1
            if c >= 0:
                m = k-c
                ans -= mods[m]
                ans %= MOD
print(ans)
