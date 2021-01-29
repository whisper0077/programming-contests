for t in range(int(input())):
    n = int(input())
    *c, = map(int, input().split())
    *b, = map(int, input().split())
    *a, = map(int, input().split())

    now = c[1]+abs(a[1]-b[1])+1
    ans = now
    for i in range(2, n):
        if a[i] == b[i]:
            now = c[i]+1
        else:
            now = c[i]+max(abs(a[i]-b[i])+1, now-abs(a[i]-b[i])+1)
        ans = max(ans, now)
    print(ans)
