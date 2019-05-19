T = int(input())
for t in range(T):
    P, Q = map(int, input().split())
    v = [0] * (10**6)
    h = [0] * (10**6)
    for p in range(P):
        x, y, d = input().split()
        x, y = int(x), int(y)
        if d == 'N':
            v[y + 1] += 1
        elif d == 'S':
            v[0] += 1
            v[y] -= 1
        elif d == 'E':
            h[x + 1] += 1
        elif d == 'W':
            h[0] += 1
            h[x] -= 1

    for i in range(1, Q + 1):
        h[i] += h[i - 1]
        v[i] += v[i - 1]

    ax, ay = 0, 0
    for i in range(Q + 1):
        if h[ax] < h[i]:
            ax = i
        if v[ay] < v[i]:
            ay = i
    print("Case #{}: {} {}".format(t + 1, ax, ay))
