import UnionFind

if __name__ == "__main__":
    # ABC065 D
    N = 3
    xy = [[1, 5], [3, 9], [7, 8]]
    x, y = [], []
    for i in range(N):
        x.append([xy[i][0], i])
        y.append([xy[i][1], i])

    e = []
    for i in range(N-1):
        e.append([abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]])
        e.append([abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]])
    e.sort()

    # クラスカル法による最小全域木
    uf = UnionFind.UnionFind(N)
    ans = 0
    for w, s, t in e:
        if not uf.same(s, t):
            uf.union(s, t)
            ans += w

    print(ans)
