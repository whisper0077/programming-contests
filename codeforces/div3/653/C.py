for t in range(int(input())):
    n = int(input())
    s = list(input().strip())
    c = 0
    ans = 0
    for i in range(n):
        if s[i] == "(":
            c += 1
        else:
            c -= 1
            if c < 0:
                c = 0
                ans += 1
    print(ans)
