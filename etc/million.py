import itertools
import random

cardsList = [
    [
        [500, 10],
        [400, 9],
        [300, 1],
        [200, 10],
        [200, 1],
        [500, 10],
        [200, 10],
        [180, 10],
        [180, 10],
        [400, 9]
    ],
    [
        [1, 1000],
        [1, 1000],
        [1, 1000],
        [1, 1000],
        [10, 1],
        [10, 1],
        [10, 1],
        [10, 1],
        [1000, 1]
    ],
    [
        [1, 100],
        [2, 0],
        [1, 0],
        [1, 0],
        [1, 0],
        [1, 0],
        [24, 0],
        [25, 0],
        [25, 0],
        [25, 0]
    ],
    [
        [2, 0],
        [1, 100],
        [1, 0],
        [1, 0],
        [1, 0],
        [1, 0],
        [24, 0],
        [25, 0],
        [25, 0],
        [25, 0]
    ]
]


def solve(cards):
    N = len(cards)      # 手持ちカード数
    W = 5               # デッキに組み込める数
    S = 1000 * W + 1    # W枚選んだときの総スキルレベル

    # 手持ちカードn枚目までからw枚選択し、総スキルレベルごとのvalue最大値を求める
    dp = [[[-float('inf')]*(S+1) for j in range(W+1)] for i in range(N+1)]
    for n in range(N+1):
        dp[n][0][0] = 0

    for n in range(1, N+1):
        v, l = cards[n-1]
        for w in range(1, min(n+1, W+1)):
            for s in range(S+1):
                if (s-l) >= 0:
                    dp[n][w][s] = max(dp[n-1][w][s], dp[n-1][w-1][s-l]+v)
                else:
                    dp[n][w][s] = dp[n-1][w][s]

    # スキルレベルとvalueペアから最大となるスキルレベルを選択する
    total = 0
    lv = 0
    for s in range(S+1):
        v = dp[N][W][s]*(100+s)//100
        if v > total:
            total = v
            lv = s

    # デッキ復元
    deck = []
    n, w = N, W
    while w > 0:
        v = dp[n][w][lv]
        cv, cl = cards[n-1]
        pv = dp[n-1][w-1][lv-cl]
        if (pv+cv) == v:
            deck.append([cv, cl])
            lv = lv-cl
            w -= 1
        n -= 1

    # 検算(brute force)
    check = 0
    checkDeck = []
    for comb in itertools.combinations(cards, W):
        v, l = 0, 0
        for a, b in comb:
            v += a
            l += b
        t = v*(100+l)//100
        if t > check:
            check = t
            checkDeck = comb

    return total == check, total, sorted(deck), check, sorted(checkDeck)


for i, cards in enumerate(cardsList):
    print(f"q[{i}]")
    ok, dp, dpd, bf, bfd = solve(cards)
    print("dp", dp, dpd)
    print("bf", bf, bfd)

for i in range(100):
    cards = []
    for j in range(10):
        cards.append([random.randint(0, 10000), random.randint(0, 12)])
    ok, dp, dpd, bf, bfd = solve(cards)
    if not ok:
        print("dp", dp, dpd)
        print("bf", bf, bfd)
