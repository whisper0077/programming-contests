
def inCircle(x, y, r, x1, y1):
    d = (x-x1)*(x-x1)+(y-y1)*(y-y1)
    return d < r*r


def leastBorders(xs, ys, rs, x1, y1, x2, y2):
    c = 0
    for i in range(len(xs)):
        x, y, r = xs[i], ys[i], rs[i]
        if inCircle(x, y, r, x1, y1) != inCircle(x, y, r, x2, y2):
            c += 1
    return c


q = [
    [
        [0, -6, 6],
        [0, 1, 2],
        [2, 2, 2],
        -5, 1, 5, 1
    ],
    [
        [1, -3, 2, 5, -4, 12, 12],
        [1, -1, 2, 5, 5, 1, 1],
        [8, 1, 2, 1, 1, 1, 2],
        -5, 1, 12, 1
    ],
    [
        [-3, 2, 2, 0, -4, 12, 12, 12],
        [-1, 2, 3, 1, 5, 1, 1, 1],
        [1, 3, 1, 7, 1, 1, 2, 3],
        2, 3, 13, 2
    ]
]

for v in q:
    print(leastBorders(*v))
