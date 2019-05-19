n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]


def loadnum(p):
    # Pで荷物がいくつ詰めるかを計算
    ni = 0
    for _ in range(k):
        s = 0
        while (s+w[ni]) <= p:
            s += w[ni]
            ni += 1
            if ni == n:
                return n
    return ni


# Pの数を2分探索で求める
lp, rp = 0, 10000*100000
while lp < rp:
    mp = (lp+rp)//2
    # 探索するPで荷物をいくつ詰めるか求める
    num = loadnum(mp)
    if num >= n:
        rp = mp
    else:
        lp = mp+1

print(lp)
