from collections import deque

for t in range(int(input())):
    n, x = map(int, input().split())
    *a, = map(int, input().split())
    q = deque([[v, 1] for v in a])
    ans = 0
    while q:
        v, m = q.popleft()
        ans += v*m
        if v % x == 0:
            q.append([v//x, m*x])
        else:
            break

    while q:
        v, m = q.popleft()
        ans += v*m
    print(ans)
