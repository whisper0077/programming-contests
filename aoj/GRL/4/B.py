v, e = map(int, input().split())
indeg = [0]*v
uv = [[] for _ in range(v)]
for i in range(e):
    s, t = map(int, input().split())
    uv[s].append(t)
    indeg[t] += 1

'''
topologicalSort
トポロジカルソート
閉路のない有向グラフの手順を表す

深さ優先でも出来る（最終到達点から頂点を入れていく）が、
再帰になるため幅優先のほうが良い
'''
visited = [False]*v
ans = []
for i in range(v):
    if indeg[i] == 0 and not visited[i]:
        q = [i]
        visited[i] = True
        while len(q) > 0:
            u = q.pop(0)
            ans.append(u)
            for v in uv[u]:
                indeg[v] -= 1
                if indeg[v] == 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)

for v in ans:
    print(v)
