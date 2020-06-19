n = int(input())
h, w = 3+n*2, 3+n*2
d = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 2],
    [2, 0], [2, 1], [2, 2]
]
ans = []
m = [[False]*w for _ in range(h)]
for y in range(0, h-1, 2):
    for x in range(0, w-1, 2):
        if y == x:
            for dy, dx in d:
                if not m[y+dy][x+dx]:
                    ans.append([x+dx, y+dy])
                    m[y+dy][x+dx] = True

print(len(ans))
for x, y in ans:
    print(x, y)
