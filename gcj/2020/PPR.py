T = int(input())
for t in range(T):
    N = int(input())
    se = [list(map(int, input().split()))+[i] for i in range(N)]
    se = sorted(se, key=lambda x: x[0])
    o = [""]*N
    ok = True
    c, j = [0, 0], [0, 0]
    for i in range(N):
        s, e, n = se[i]
        if c[1] <= s:
            c = [s, e]
            o[n] = "C"
        elif j[1] <= s:
            j = [s, e]
            o[n] = "J"
        else:
            ok = False
            break
    ans = "IMPOSSIBLE"
    if ok:
        ans = "".join(o)
    print("Case #{}: {}".format(t+1, ans))
