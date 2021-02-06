H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]
ans = 0
for y in range(1, H):
    for x in range(1, W):
        b = 0
        for dy in range(-1, 1):
            for dx in range(-1, 1):
                if S[y+dy][x+dx] == "#":
                    b += 1
        if b % 2 == 1:
            ans += 1
print(ans)
