from operator import add, mul, sub, or_


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


M = 10**6
N, K = map(int, input().split())
seg = SegmentTree([0]*M, max, 0)
ans = 0
for i in range(N):
    a = int(input())
    t = seg.query(max(0, a-K), min(M, a+K+1))+1
    seg.update(a, t)
    ans = max(ans, t)
print(ans)
