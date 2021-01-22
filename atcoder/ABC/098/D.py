from itertools import accumulate
from operator import add, mul, sub, or_, xor


class SegmentTree:
    '''
    セグメント木(遅延ではない)
    1-indexd セグメント木
    values : 値の配列
    op : 区間に対する関数
    ie : 初期値
    '''

    def __init__(self, values, op, ie):
        self.values = values
        vlen = len(values)
        self.op = op
        self.size = 2 ** (vlen-1).bit_length()
        self.tree = [ie]*self.size + self.values + [ie]*(self.size-vlen)
        self.ie = ie

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.op(self.tree[i*2], self.tree[i*2+1])

    def update(self, i, v):
        i += self.size
        self.tree[i] = v
        while i > 0:
            i //= 2
            self.tree[i] = self.op(self.tree[i*2], self.tree[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        ret = self.ie
        while l < r:
            if l & 1:
                ret = self.op(ret, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.op(ret, self.tree[r])
            l //= 2
            r //= 2
        return ret


N = int(input())
*A, = map(int, input().split())
x = SegmentTree(A, xor, 0)
s = [0]+list(accumulate(A))

ans = 0
for i in range(N):
    l, r = i, N
    while (r-l) > 1:
        m = (l+r)//2
        if (s[m+1]-s[i]) == x.query(i, m+1):
            #print("ok", i, m, "sum=", s[m+1]-s[i], "xor=", x.query(i, m+1))
            l = m
        else:
            r = m
    ans += l-i+1
print(ans)
