for t in range(int(input())):
    p, f = map(int, input().split())
    cnts, cntw = map(int, input().split())
    s, w = map(int, input().split())

    if s > w:
        s, w = w, s
        cnts, cntw = cntw, cnts

    ans = 0
    for i in range(cnts+1):
        ms, fs = i, cnts-i
        ms = min(ms, p//s)
        fs = min(fs, f//s)

        rp = p-ms*s
        rf = f-fs*s

        mw, fw = rp//w, rf//w
        mw = min(mw, cntw)
        fw = min(fw, cntw-mw)
        tmp = ms+fs+mw+fw
        if tmp > ans:
            ans = tmp

    print(ans)
