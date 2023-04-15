for t in range(int(input())):
    r, c = map(int, input().split())

    print("Case #{}:".format(t+1))
    for y in range(r*2+1):
        p = "+-"
        if y % 2 == 1:
            p = "|."
        if y < 2:
            s = ".."+p*(c-1)+p[0]
        else:
            s = p*c+p[0]
        print(s)
