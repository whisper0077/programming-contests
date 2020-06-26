from collections import defaultdict, deque

N, M = map(int, input().split())
e = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    e[u].append(v)

'''
頂点を%3で考える(1つの頂点にを3つに分解する)
(u,0)->(v,1)
(v,1)->(u,2)
(u,2)->(v,0)
これをBFSする
'''

S, T = map(int, input().split())
q = deque([[S, 0]])
dist = [[-3]*3 for _ in range(N+1)]
dist[S][0] = 0
while q:
    u, c = q.popleft()
    for v in e[u]:
        step = (c+1) % 3
        if dist[v][step] < 0:
            dist[v][step] = c+1
            q.append([v, c+1])

print(dist[T][0]//3)

'''
def kenkenpa(s, visited):
    res = []
    for v1 in e[s]:
        if visited[v1][1]:
            continue
        visited[v1][1] = True
        for v2 in e[v1]:
            if visited[v2][2]:
                continue
            visited[v2][2] = True
            for v3 in e[v2]:
                if visited[v3][0]:
                    continue
                visited[v3][0] = True
                res.append(v3)
    return res


N, M = map(int, input().split())
e = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    e[u].append(v)

S, T = map(int, input().split())
q = deque([[S, 0]])
visited = [[False]*3 for _ in range(N+1)]
visited[S][0] = True
ans = -1
while q:
    u, c = q.popleft()
    if u == T:
        ans = c
        break
    l = kenkenpa(u, visited)
    for v in l:
        q.append([v, c+1])
print(ans)
'''
