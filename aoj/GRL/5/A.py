import sys
sys.setrecursionlimit(1000000)

n = int(input())
e = [[] for _ in range(n)]
weights = {}
for i in range(n-1):
    s, t, w = map(int, input().split())
    e[s].append(t)
    e[t].append(s)
    weights[(s, t)] = w
    weights[(t, s)] = w


def dfs(v, w, visited):
    r = [w, v]
    visited[v] = True
    for tv in e[v]:
        if not visited[tv]:
            r = max([dfs(tv, w+weights[(v, tv)], visited), r])
    return r


def fartheast(v):
    visited = [False]*n
    return dfs(v, 0, visited)


'''
木の直径
以下のアルゴリズムで求められる
'''
xw, x = fartheast(0)
yw, y = fartheast(x)
print(yw)
