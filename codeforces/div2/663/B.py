for t in range(int(input())):
    n, m = map(int, input().split())
    a = [list(input().strip()) for _ in range(n)]
    ans = 0
    for y in range(n-1):
        if a[y][m-1] != "D":
            ans += 1
    for x in range(m-1):
        if a[n-1][x] != "R":
            ans += 1
    print(ans)
