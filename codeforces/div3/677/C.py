for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    a = [10**10]+a+[10**10]

    ans, m = -1, 0
    for i in range(1, n+1):
        if a[i-1] < a[i] or a[i] > a[i+1]:
            if a[i] > m:
                m = a[i]
                ans = i
    print(ans)
