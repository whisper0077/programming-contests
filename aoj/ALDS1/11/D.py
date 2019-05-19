n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    s, t = map(int, input().split())
    g[s].append(t)
    g[t].append(s)

# dfsで連結成分を求める
r = [0]*n
for i in range(n):
    if r[i] == 0:
        l = [i]
        while len(l) > 0:
            u = l.pop(-1)
            r[u] = i+1
            for v in g[u]:
                if r[v] == 0:
                    l.append(v)

q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    if r[s] == r[t]:
        print("yes")
    else:
        print("no")
'''
この方法はメモリをO(n**2)使い、また多くの検索回数を必要とするため駄目
n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]

for i in range(m):
    s, t = map(int, input().split())
    g[s][t] = 1
    g[t][s] = 1

q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    l = [s]
    d = [0]*n
    ans = "no"
    while len(l) > 0:
        u = l.pop(0)
        if u == t:
            ans = "yes"
            break
        for i, v in enumerate(g[u]):
            if v == 1 and d[i] == 0:
                d[i] = 1
                l.append(i)
    print(ans)
'''
