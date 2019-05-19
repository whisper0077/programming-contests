from collections import deque
H, W = map(int, input().split())
hw = [list(input().strip()) for _ in range(H)]
b = deque()
for h in range(H):
    for w in range(W):
        if hw[h][w] == '#':
            b.append([h, w, 0])

ans = 0
while len(b) > 0:
    h, w, d = b.popleft()
    d += 1
    for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nh, nw = h + y, w + x
        if nh >= 0 and nh < H and nw >= 0 and nw < W and hw[nh][nw] == '.':
            b.append([nh, nw, d])
            if ans < d:
                ans = d
            hw[nh][nw] = "#"
print(ans)