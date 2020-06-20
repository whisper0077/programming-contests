def factorList(n):
    f = {}
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f[i] = c
            c = 0
    if n != 1:
        f[n] = 1
    return f


T = int(input())
for t in range(T):
    n = int(input())
    if n == 1:
        print("FastestFinger")
    elif n == 2:
        print("Ashishgup")
    elif n % 2 == 1:
        print("Ashishgup")
    else:
        d = 1
        fl = factorList(n)
        o = 0
        for k, v in fl.items():
            if k % 2 == 1:
                o += v
        if fl[2] == 1:
            if o > 1:
                print("Ashishgup")
            else:
                print("FastestFinger")
        else:
            if o > 0:
                print("Ashishgup")
            else:
                print("FastestFinger")
