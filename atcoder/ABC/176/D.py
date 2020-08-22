from collections import deque
H, W = map(int, input().split())
cy, cx = map(int, input().split())
dy, dx = map(int, input().split())
cy -= 1
cx -= 1
dy -= 1
dx -= 1
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
S = [input() for _ in range(H)]

worps = [[float('inf')]*W for _ in range(H)]
q = deque([[cy, cx]])

worps[cy][cx] = 0
while q:
    y, x = q.popleft()
    worp = worps[y][x]

    for h, w in d:
        ny, nx = y+h, x+w
        if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "." and worp < worps[ny][nx]:
            worps[ny][nx] = worp
            q.appendleft([ny, nx])

    worp += 1
    for h in range(-2+y, 3+y):
        for w in range(-2+x, 3+x):
            if 0 <= h < H and 0 <= w < W and S[h][w] == "." and worp < worps[h][w]:
                worps[h][w] = worp
                q.append([h, w])

ans = worps[dy][dx]
if ans != float('inf'):
    print(ans)
else:
    print(-1)
