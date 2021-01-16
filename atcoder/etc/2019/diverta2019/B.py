R, G, B, N = map(int, input().split())
ans = 0
for r in range(0, 3001, R):
    for g in range(0, 3001, G):
        b = N-r-g
        if b >= 0 and b % B == 0:
            ans += 1
print(ans)
