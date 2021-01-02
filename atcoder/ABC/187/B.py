n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    x0, y0 = xy[i]
    for j in range(i+1, n):
        x1, y1 = xy[j]
        if abs(y1-y0) <= abs(x1-x0):
            ans += 1
print(ans)
