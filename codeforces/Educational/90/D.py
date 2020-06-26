
def KadanesAlgorithm(a):
    '''
    最大部分配列をDPでとく
    https://ark4rk.hatenablog.com/entry/2018/01/08/002508
    '''
    res = -float('inf')
    s = 0
    for i in range(len(a)):
        s = max(s+a[i], a[i])
        res = max(s, res)
    return res


for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())

    ans = 0 if (n-1) % 2 == 1 else a[n-1]
    evens, odds = [], []
    for i in range(n-1):
        if i % 2 == 0:
            ans += a[i]
            evens.append(a[i+1]-a[i])
        else:
            odds.append(a[i]-a[i+1])

    d = max(KadanesAlgorithm(evens), KadanesAlgorithm(odds))
    ans = max(ans, ans+d)
    print(ans)
