n = int(input())
g = [[] for i in range(n)]
for i in range(n):
    *v, = map(int, input().split())
    for j in range(n):
        if v[j] < 0:
            v[j] = 10000
    g[i] = v

'''
プリムのアルゴリズム
正直版
'''
ans = 0
t = [0]
v = [i for i in range(1, n)]
while len(t) < n:
    u = [2000, 0, 0]
    for tv in t:
        for vv in v:
            if g[tv][vv] < u[0]:
                u = [g[tv][vv], tv, vv]
    ans += u[0]
    t.append(u[2])
    v.remove(u[2])
print(ans)
