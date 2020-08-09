from collections import deque

for t in range(int(input())):
    n = int(input())
    q = deque()
    for i in range(n, 0, -1):
        if i % 2 == 0:
            q.append(i)
        else:
            q.appendleft(i)
    print(*q)
