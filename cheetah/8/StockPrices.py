'''
貪欲法

最終月からさかのぼり、利益率が最大になるタイミングで買っていく
'''


def maximumEarnings(initial, monthly, prices):
    last = prices.pop(-1)
    money = initial

    buys = [False]*len(prices)
    proportions = [0]*len(prices)
    maxp = 0
    for i in range(len(prices)-1, -1, -1):
        for j in range(len(prices[i])):
            p = last[j]/prices[i][j]-1.0
            if 0 < p and p > maxp:
                maxp = p
                buys[i] = True
                proportions[i] = p

    ans = 0
    for i in range(len(prices)):
        if buys[i]:
            ans += proportions[i]*money
            money = 0
        money += monthly
    return ((ans*2+1)//2)


q = [
    [
        1000,
        0,
        [
            [10, 20, 30],
            [15, 24, 32]
        ]
    ],
    [
        500,
        0,
        [
            [10, 20, 30]
        ]
    ],
    [
        100,
        20,
        [
            [40, 50, 60],
            [37, 48, 55],
            [100, 48, 50],
            [105, 48, 47],
            [110, 50, 52],
            [110, 50, 52],
            [110, 51, 54],
            [109, 49, 53]
        ]
    ]
]
for v in q:
    print(maximumEarnings(*v))
