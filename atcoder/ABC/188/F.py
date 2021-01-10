from functools import lru_cache
X, Y = map(int, input().split())

'''
YをXにする操作と考える
A -> +1
B -> -1
C -> /2
とすると、
AB,BA -> 何もしない
AAC,BBC -> CA,CBに置き換え可能
上記操作は考えなくて良くなる

よって遷移はC or AC or BCで、2で割り切れるかどうかで変わる
操作回数は |X-y| or C(+1) or AC(+2) or BC(+2)となる

毎回関数を呼び出したときの引数の変化先はたかだか2個で、//2されていくのでlog(Y)個程度しかない
'''


@lru_cache(None)
def solve(y):
    if X >= y:
        return X-y
    r = y-X
    if y % 2 == 0:
        r = min(r, solve(y//2)+1)
    else:
        r = min(r, solve((y+1)//2)+2, solve((y-1)//2)+2)
    return r


print(solve(Y))
