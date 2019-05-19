'''
セグメント木
配列バージョン
'''

N, Q = map(int, input().split())
pn = 1
while pn < N:
    pn *= 2
N = pn
A = [0]*(2*N-1)


def add(x, y):
    n = N+x-1
    A[n] += y
    while n > 0:
        n = (n-1)//2
        A[n] += y


def getSum(k, x, y, s, t):
    '''
    範囲[x,y)
    区間[s,t)
    '''
    #print("sum ", x, y, s, t)
    # 交差しない
    if x >= t or y <= s:
        #print("no intersect", x, y, s, t)
        return 0
    # 範囲が区間を包含する
    if x <= s and t <= y:
        #print("intersect ", x, y, s, t)
        return A[k]

    # それ以外
    #print("other ", x, y, s, t)
    lv = getSum(2*k+1, x, y, s, (s+t)//2)
    rv = getSum(2*k+2, x, y, (s+t)//2, t)
    return lv+rv


for i in range(Q):
    com, x, y = map(int, input().split())
    if com == 0:
        add(x-1, y)
    else:
        print(getSum(0, x-1, y, 0, N))
    # print(A)
