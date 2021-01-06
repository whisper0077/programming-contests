import bisect

for t in range(int(input())):
    n = int(input())
    hw = []
    for i in range(n):
        h, w = map(int, input().split())
        hw.append([h, w, i+1])

    shw = sorted(hw)
    mw = [[shw[0][1], shw[0][2]]]
    for i in range(1, n):
        w, j = mw[-1]
        if shw[i][1] < w:
            w, j = shw[i][1], shw[i][2]
        mw.append([w, j])

    ans = []
    for h, w, _ in hw:
        a = -1
        for y, x in [[h, w], [w, h]]:
            i = bisect.bisect_left(shw, [y, 0])-1
            if i >= 0 and mw[i][0] < x:
                a = mw[i][1]
                break
        ans.append(a)
    print(*ans)
