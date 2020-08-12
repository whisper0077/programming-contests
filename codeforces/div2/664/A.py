for t in range(int(input())):
    r, g, b, w = map(int, input().split())
    ans = "No"
    for i in range(2):
        o = 0
        for c in [r, g, b, w]:
            if c % 2 == 1:
                o += 1
        if o <= 1:
            ans = "Yes"
            break
        if r > 0 and g > 0 and b > 0:
            r -= 1
            g -= 1
            b -= 1
            w += 3
        else:
            break
    print(ans)
