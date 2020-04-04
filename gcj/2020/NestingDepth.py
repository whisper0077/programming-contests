T = int(input())
for t in range(T):
    s = "0"+input().strip()+"00"
    ans = ""
    for i in range(0, len(s)-1):
        l, r = int(s[i]), int(s[i+1])
        d = l-r
        if d > 0:
            ans += s[i] + ")"*d
        elif d < 0:
            ans += s[i] + "("*(-d)
        else:
            ans += s[i]
    print("Case #{}: {}".format(t+1, ans[1:-1]))
