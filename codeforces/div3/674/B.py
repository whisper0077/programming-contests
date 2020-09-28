for t in range(int(input())):
    n, m = map(int, input().split())
    ans = "NO"
    for i in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c:
            ans = "YES"

    if m % 2 == 1:
        ans = "NO"

    print(ans)
