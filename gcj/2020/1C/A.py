H = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0], 'P': [0, 0]}
T = int(input())
for t in range(T):
    x, y, m = input().split()
    x = int(x)
    y = int(y)
    ans = "IMPOSSIBLE"
    p = 0
    for s in 'P'+m:
        d = H[s]
        x += d[0]
        y += d[1]
        if abs(x)+abs(y) <= p:
            ans = p
            break
        p += 1
    print("Case #{}: {}".format(t+1, ans))
