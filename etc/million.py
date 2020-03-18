import itertools

N = int(input())
W = 5
S = 1001 * N
cards = [list(map(int, input().split())) for i in range(N)]

# 手持ちカードn枚目までからw枚選択し、総スキルレベルごとのvalue最大値を求める
dp = [[[-1]*(S+1) for j in range(W+1)] for i in range(N+1)]
dp[0][0][0] = 0

for n in range(1, N+1):
    v, l = cards[n-1]
    for w in range(1, min(n+1, W+1)):
        for s in range(S+1):
            if (s-l) >= 0 and dp[n-1][w-1][s-l] >= 0:
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
    for cv, cl in cards:
        pv = dp[n-1][w-1][lv-cl]
        if (pv+cv) == v:
            deck.append([cv, cl])
            lv = lv-cl
            w -= 1
            found = True
            break
    n -= 1

print("dp         ", total, deck)

# 検算
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
print("brute force", check, checkDeck)
