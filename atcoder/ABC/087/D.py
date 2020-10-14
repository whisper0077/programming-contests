from collections import deque

N, M = map(int, input().split())
g = {}

for i in range(M):
    l, r, d = map(int, input().split())
    if l not in g:
        g[l] = {}
    if r not in g:
        g[r] = {}
    g[l][r] = d
    g[r][l] = -d

if M <= 2:
    print("Yes")
else:
    ans = "Yes"
    d = [-1]*(N+1)
    use = [False]*(N+1)

    for s in g.keys():
        if use[s]:
            continue

        use[s] = True
        d[s] = 0
        q = deque()
        q.append(s)

        while q:
            v = q.popleft()
            if v in g:
                for u, uw in g[v].items():
                    nd = d[v]+uw
                    if not use[u]:
                        d[u] = nd
                        q.append(u)
                        use[u] = True
                    else:
                        if u != s and d[u] != nd:
                            ans = "No"
                            q.clear()
                            break

    print(ans)
