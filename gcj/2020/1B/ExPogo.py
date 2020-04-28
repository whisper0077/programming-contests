T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    if x % 2 == y % 2:
        print("Case #{}: IMPOSSIBLE".format(t+1))
        continue

    ans = ""
    while x != 0 or y != 0:
        if x == 1 and y == 0:
            p = [[-1, 0, "E"]]
        elif x == 0 and y == 1:
            p = [[0, -1, "N"]]
        elif x % 2 == 1:
            p = [[1, 0, "W"], [-1, 0, "E"]]
        else:
            p = [[0, 1, "S"], [0, -1, "N"]]
        for dx, dy, d in p:
            nx = (x+dx)//2
            ny = (y+dy)//2
            if (nx == 0 and ny == 0) or (nx % 2 != ny % 2):
                x = nx
                y = ny
                ans += d
                break

    print("Case #{}: {}".format(t+1, ans))
