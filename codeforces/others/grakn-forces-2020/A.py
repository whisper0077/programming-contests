for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())
    *c, = map(int, input().split())
    ans = [0]*n
    ans[-1] = a[-1]
    for i in range(n-1):
        for v in [a[i], b[i], c[i]]:
            if v != ans[i-1] and v != ans[i+1]:
                ans[i] = v
                break
    print(*ans)
