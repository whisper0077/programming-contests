# 部分和問題
# n個の数字を組み合わせてkが作れるかどうか


class DFS:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def solve(self, i, s):
        if s == self.k:
            return True
        if i >= len(self.n):
            return False
        if self.solve(i+1, s+self.n[i]):
            return True
        if self.solve(i+1, s):
            return True
        return False


print(DFS([1, 2, 4, 7], 13).solve(0, 0))
print(DFS([1, 2, 4, 7], 15).solve(0, 0))

# 迷路を解く
# わかりやすくするため、外堀を埋めておく


class BFS:
    def __init__(self):
        self.yx = [1, 2]
        self.maze = [
            list("############"),
            list("##S######.##"),
            list("#......#..##"),
            list("#.#.##.##.##"),
            list("#.#........#"),
            list("###.##.#####"),
            list("#....#....##"),
            list("#.#######.##"),
            list("#....#.....#"),
            list("#.####.###.#"),
            list("#....#...G##"),
            list("############"),
        ]

    def solve(self):
        r = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = [self.yx]
        q[0].append(0)
        while len(q) > 0:
            yxz = q.pop(0)
            if self.maze[yxz[0]][yxz[1]] == 'G':
                return yxz[2]

            self.maze[yxz[0]][yxz[1]] = '#'

            for dyx in r:
                y, x = yxz[0]+dyx[0], yxz[1]+dyx[1]
                if self.maze[y][x] != '#':
                    q.append([y, x, yxz[2]+1])
        return -1


print(BFS().solve())

# 辞書順最小


class BestCowLine:
    def __init__(self):
        self.n = 6
        self.s = list("ACDBCB")

    def solve(self):
        t = ""
        while len(self.s) > 0:
            if self.s[0] == self.s[-1]:
                if self.s < self.s[::-1]:
                    t += self.s[0]
                    self.s = self.s[1:]
                else:
                    t += self.s[-1]
                    self.s = self.s[:-1]
            elif self.s[0] < self.s[-1]:
                t += self.s[0]
                self.s = self.s[1:]
            else:
                t += self.s[-1]
                self.s = self.s[:-1]
        return t


print(BestCowLine().solve())

# Fence Repair


class FenceRepair:
    def __init__(self):
        self.n = 5
        self.l = [3, 4, 5, 1, 2]

    def solve(self):
        ans = 0
        while self.n > 1:
            self.l.sort()
            t = self.l[0]+self.l[1]
            self.l = self.l[2:]
            self.l.append(t)
            ans += t
            self.n -= 1
        return ans

    def solve2(self):
        self.l.sort()
        ans = 0
        while self.n > 1:
            # 一番小さい葉の２つを調べる
            m1, m2 = 0, 1
            if self.l[m1] > self.l[m2]:
                m1, m2 = m2, m1
            for i in range(2, self.n):
                if self.l[i] < self.l[m1]:
                    m2 = m1
                    m1 = i
                elif self.l[i] < self.l[m2]:
                    m2 = i

            # 葉を統合
            t = self.l[m1]+self.l[m2]
            ans += t

            # nをへらすため、m1がn-1の場合は修正
            if m1 == (self.n-1):
                m1, m2 = m2, m1
            self.l[m1] = t
            self.l[m2] = self.l[self.n-1]
            self.n -= 1
        return ans


print(FenceRepair().solve())
print(FenceRepair().solve2())
