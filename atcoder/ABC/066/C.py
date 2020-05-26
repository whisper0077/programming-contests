from collections import deque
n = int(input())
*a, = map(int, input().split())
b = deque()
for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])

if n % 2 == 1:
    b.reverse()

print(" ".join([str(v) for v in b]))
