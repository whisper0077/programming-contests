
class Solver:
    def __init__(self, k, e, w, s, n):
        self.k = k
        self.p = {"E": e/100, "W": w/100, "S": s/100, "N": n/100}
        self.m = [[0]*15 for _ in range(15)]
        self.dxy = {"E": [1, 0], "W": [-1, 0], "S": [0, -1], "N": [0, 1]}

    def solve(self, k, p, x, y):
        if k >= self.k:
            return 1

        self.m[y][x] = 1

        ans = 0

        for s in "EWSN":
            dx, dy = self.dxy[s]
            nx = x + dx
            ny = y + dy
            if self.p[s] > 0 and self.m[ny][nx] == 0:
                ans += self.solve(k+1, p+s, nx, ny) * self.p[s]

        self.m[y][x] = 0
        return ans


q = [
    [1, 25, 25, 25, 25],
    [2, 25, 25, 25, 25],
    [14, 50, 50, 0, 0],
]
for v in q:
    s = Solver(*v)
    print(s.solve(0, "", 0, 0))
