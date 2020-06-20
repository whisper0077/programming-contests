from collections import deque
T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    mz = [list("#"+input().strip()+"#") for _ in range(n)]
    mz = [["#"]*(m+2)] + mz + [["#"]*(m+2)]

    ok = True
    g = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if mz[i][j] == "B":
                for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    y, x = i+dy, j+dx
                    if mz[y][x] == ".":
                        if y == n and x == m:
                            ok = False
                        mz[y][x] = "#"
                    elif mz[y][x] == "G":
                        ok = False
                        break
            elif mz[i][j] == "G":
                g += 1

    if g == 0:
        print("Yes")
        continue
    if not ok:
        print("No")
        continue

    visited = {}
    q = deque()
    q.append([n, m])
    while len(q) > 0:
        y, x = q.popleft()
        if mz[y][x] == "G":
            g -= 1
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ny, nx = y+dy, x+dx
            if (ny, nx) not in visited and mz[ny][nx] != "#":
                visited[(ny, nx)] = True
                q.append([ny, nx])
    print("Yes" if g == 0 else "No")
