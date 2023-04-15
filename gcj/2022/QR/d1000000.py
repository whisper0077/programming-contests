for t in range(int(input())):
    n = int(input())
    *s, = map(int, input().split())
    s.sort()

    ans = 0
    for i in range(n):
        m = ans+1
        if m <= s[i]:
            ans += 1

    print("Case #{}: {}".format(t+1, ans))
