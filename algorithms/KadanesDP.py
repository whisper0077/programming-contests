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


if __name__ == "__main__":
    # codeforces/Educational/90/D.py
    print(KadanesAlgorithm([1, 1, -1, 1, -4]))
