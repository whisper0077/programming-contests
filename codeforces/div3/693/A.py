for t in range(int(input())):
    w, h, n = map(int, input().split())
    ans = 1
    while True:
        if w % 2 == 0:
            w //= 2
        elif h % 2 == 0:
            h //= 2
        else:
            break
        ans *= 2
    if ans >= n:
        print("Yes")
    else:
        print("No")
