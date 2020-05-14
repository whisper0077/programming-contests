T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    *b, = map(int, input().split())
    a.sort()
    b.sort(key=lambda x: -x)

    ans = sum(a)
    for i in range(n):
        if k <= 0:
            break
        if a[i] < b[i]:
            ans += b[i]-a[i]
            k -= 1
    print(ans)
