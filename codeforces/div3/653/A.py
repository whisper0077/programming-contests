for t in range(int(input())):
    x, y, n = map(int, input().split())
    z = n//x
    ans = x*z+y
    if ans > n:
        ans -= x
    print(ans)
