import math
n = int(input())

cos60 = math.cos(math.radians(60))
sin60 = math.sin(math.radians(60))


def koch(d, p1, p2):
    if d == 0:
        return
    s = [
        (2.0*p1[0]+1.0*p2[0])/3.0,
        (2.0*p1[1]+1.0*p2[1])/3.0
    ]
    t = [
        (1.0*p1[0]+2.0*p2[0])/3.0,
        (1.0*p1[1]+2.0*p2[1])/3.0
    ]
    u = [
        (t[0]-s[0])*cos60 - (t[1]-s[1])*sin60 + s[0],
        (t[0]-s[0])*sin60 + (t[1]-s[1])*cos60 + s[1]
    ]

    koch(d-1, p1, s)
    print(f"{s[0]} {s[1]}")
    koch(d-1, s, u)
    print(f"{u[0]} {u[1]}")
    koch(d-1, u, t)
    print(f"{t[0]} {t[1]}")
    koch(d-1, t, p2)
    return


print(f"{0} {0}")
koch(n, [0, 0], [100, 0])
print(f"{100} {0}")
