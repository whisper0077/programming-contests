for t in range(int(input())):
    x = int(input())
    ans = 0
    for i in range(1, 10):
        for j in range(1, 5):
            v = int(str(i)*j)
            ans += j
            if v == x:
                x = -1
                break
        if x < 0:
            break
    print(ans)
