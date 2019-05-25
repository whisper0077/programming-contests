N, M = map(int, input().split())
x, y = -1, 10**6
for i in range(M):
    l, r = map(int, input().split())
    x = max(l, x)
    y = min(r, y)
print(max(0, y - x + 1))
