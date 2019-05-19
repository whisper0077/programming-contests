import sys
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())

st = [[False for _ in range(V)] for _ in range(V)]

for i in range(E):
    s, t = map(int, input().split())
    st[s][t] = True
    st[t][s] = True

time = 1
prenum = [-1]*V
parent = [-1]*V
lowest = [2**32]*V

'''
関節点
あるグラフにおいて、頂点uとuから出ている辺を削除して得られるグラフが
非連結になる頂点uのこと
'''


def dfs(p, u):
    global time
    prenum[u] = time
    lowest[u] = time
    time += 1
    parent[u] = p
    for i, e in enumerate(st[u]):
        if e:
            if prenum[i] == -1:
                dfs(u, i)
                lowest[u] = min([lowest[i], lowest[u]])
            elif p != i:
                # backedge
                lowest[u] = min([prenum[i], lowest[u]])


dfs(-1, 0)

ans = set()
root = 0
for i in range(1, V):
    p = parent[i]
    if p == 0:
        root += 1
    elif prenum[p] <= lowest[i]:
        ans.add(p)

if root > 1:
    ans.add(0)

for v in sorted(ans):
    print(v)
