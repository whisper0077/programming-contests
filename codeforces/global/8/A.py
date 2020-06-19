T = int(input())
for t in range(T):
    a, b, c = map(int, input().split())
    ans = 0
    while a <= c and b <= c:
        if a >= b:
            b += a
        else:
            a += b
        ans += 1
    print(ans)
