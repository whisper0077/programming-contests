for t in range(int(input())):
    n = int(input())
    t, s = 0, -1
    for i in range(20):
        for j in range(20):
            k = 2**i*3**j
            if n == k:
                t = i
                s = j
                break

    if t <= s:
        print(s-t+s)
    else:
        print(-1)
