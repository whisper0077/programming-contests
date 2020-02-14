from collections import deque
INF = float('inf')


class Solver:
    def __init__(self, maze, sy, sx, my, mx):
        self.maze = []
        for mz in maze:
            t = []
            for s in mz:
                if s == ".":
                    t.append(INF)
                else:
                    t.append(-1)
            self.maze.append(t)
        self.maze[sy][sx] = 0
        self.sy = sy
        self.sx = sx
        self.my = my
        self.mx = mx
        self.ny = len(self.maze)
        self.nx = len(self.maze[0])

    def solve(self):
        q = deque()
        q.append([0, self.sy, self.sx])
        while len(q) > 0:
            t, ty, tx = q.popleft()
            for i in range(len(self.my)):
                y, x = ty+self.my[i], tx+self.mx[i]
                if 0 <= y and y < self.ny and 0 <= x and x < self.nx and self.maze[y][x] == INF:
                    q.append([t+1, y, x])
                    self.maze[y][x] = t+1

        ans = 0
        for mz in self.maze:
            ans = max([ans, max(mz)])
        return -1 if ans == INF else ans


q = [
    [
        [
            "...",
            "...",
            "..."
        ],
        0, 1,
        [1, 0, -1, 0],
        [0, 1, 0, -1]
    ],
    [
        [
            "x.x",
            "...",
            "xxx",
            "x.x"
        ],
        0, 1,
        [1, 0, -1, 0],
        [0, 1, 0, -1]
    ],
    [
        [
            ".......",
            "x.x.x..",
            "xxx...x",
            "....x..",
            "x....x.",
            "......."
        ],
        5, 0,
        [1, 0, -1, 0, -2, 1],
        [0, -1, 0, 1, 3, 0]
    ]
]
for v in q:
    s = Solver(*v)
    print(s.solve())
