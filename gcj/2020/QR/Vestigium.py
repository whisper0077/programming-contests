T = int(input())
for t in range(T):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    k, r, c = 0, 0, 0
    for i in range(N):
        rows = {}
        cols = {}
        for j in range(N):
            if i == j:
                k += m[i][j]
            rows[m[i][j]] = 1
            cols[m[j][i]] = 1
        if len(rows) != N:
            r += 1
        if len(cols) != N:
            c += 1
    print("Case #{}: {} {} {}".format(t+1, k, r, c))
