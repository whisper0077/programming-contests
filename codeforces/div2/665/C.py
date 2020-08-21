for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    d = min(a)
    b = sorted(a)

    ans = "YES"
    for i in range(n):
        if a[i] != b[i]:
            if b[i] % d != 0:
                ans = "NO"
                break
    print(ans)
