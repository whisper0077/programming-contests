from collections import deque
for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())

    used = [False]*n
    used[0] = True
    q = deque([0])
    ans = []
    while q:
        v = q.popleft()
        for u in range(n):
            if a[v] != a[u] and not used[u]:
                ans.append([v, u])
                q.appendleft(u)
                used[u] = True

    if len(ans) == (n-1):
        print("YES")
        for u, v in ans:
            print(u+1, v+1)
    else:
        print("NO")
