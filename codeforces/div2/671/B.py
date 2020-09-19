for t in range(int(input())):
    x = int(input())
    n = 0
    ans = 0
    p = 1
    for i in range(1, 100):
        n = n*2+p*p
        x -= n
        p *= 2
        if x < 0:
            break
        ans += 1
    print(ans)
