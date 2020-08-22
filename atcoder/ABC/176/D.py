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

# 0-1BFS
# worpせずに移動できる場合 -> 先頭に追加
# worpして移動できる場合 -> 末尾に追加
# これを最短worps数で管理していく
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

'''
from collections import deque
H, W = map(int, input().split())
cy, cx = map(int, input().split())
dy, dx = map(int, input().split())
cy -= 1
cx -= 1
dy -= 1
dx -= 1

S = [input() for _ in range(H)]

worps = [[float('inf')]*W for _ in range(H)]
used = [[False]*W for _ in range(H)]
q = deque([[cy, cx]])

worp = 0
while q:
    v = {}
    while q:
        y, x = q.popleft()
        used[y][x] = True
        worps[y][x] = min(worps[y][x], worp)

        for h in range(-2+y, 3+y):
            for w in range(-2+x, 3+x):
                if 0 <= h and h < H and 0 <= w and w < W and S[h][w] == ".":
                    v[(h, w)] = True

        for h, w in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ny, nx = y+h, x+w
            if 0 <= ny and ny < H and 0 <= nx and nx < W:
                if not used[ny][nx] and S[ny][nx] == ".":
                    q.appendleft([ny, nx])

    worp += 1
    for h, w in v.keys():
        if not used[h][w]:
            q.appendleft([h, w])
            used[h][w] = True

ans = worps[dy][dx]
if ans != float('inf'):
    print(ans)
else:
    print(-1)
'''
