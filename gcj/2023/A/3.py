for t in range(int(input())):
    n = int(input())
    *s, = map(int, input().split())
    c = 0
    cv = {}
    m = {}
    lv = ""
    for v in s:
        if v in m:
            if lv != v:
                c = -1
                break
        else:
            m[v] = c
            cv[c] = v
            c += 1
            lv = v

    ans = "IMPOSSIBLE"
    if c >= 0:
        ans = " ".join([str(cv[i]) for i in range(c)])
    print("Case #{}: {}".format(t+1, ans))

'''
1
4
3 8 8 2
1
5
3 8 2 2 8
'''
