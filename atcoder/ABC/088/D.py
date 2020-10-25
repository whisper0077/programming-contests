from collections import deque

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

used = [[False]*W for _ in range(H)]
q = deque([[0, 0, 1]])
used[0][0] = True
total = 0
while q:
    x, y, c = q.popleft()
    if x == (W-1) and y == (H-1):
        total = c
        break
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nx, ny = x+dx, y+dy
        if 0 <= nx and nx < W and 0 <= ny and ny < H and not used[ny][nx] and s[ny][nx] == ".":
            q.append([nx, ny, c+1])
            used[ny][nx] = True

if total == 0:
    print(-1)
else:
    for y in range(H):
        for x in range(W):
            if s[y][x] == ".":
                total -= 1
    print(-total)
