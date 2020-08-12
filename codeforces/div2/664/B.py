n, m, sx, sy = map(int, input().split())
sx -= 1
sy -= 1
ans = "No"
for w in range(n):
    x = (w+sx) % n
    for h in range(m):
        y = (h+sy) % m
        print(x+1, y+1)
    sy = (m-1+sy) % m
