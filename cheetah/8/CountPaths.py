MOD = 10**9+7


class HamiltonPath:
    def __init__(self, roads):
        self.roads = roads
        self.visited = [False]*len(roads)

    def countPaths(self):
        # 各場所から通らなくてはいけない道の数を出す
        counts = [r.count('Y') for r in self.roads]

        # ある場所から3つ以上通らないといけない場合は0
        for c in counts:
            if c >= 3:
                return 0

        g, f = 0, 0
        # roadsでつながっている場所をグルーピング
        for i in range(len(counts)):
            if counts[i] == 1 and not self.visited[i]:
                self.dfs(i)
                g += 1
            elif counts[i] == 0:
                self.visited[i] = True
                f += 1

        # 閉路がある場合は
        if not all(self.visited):
            return 0

        ans = 1
        for i in range(g+f):
            ans = ans*(i+1) % MOD
        for i in range(g):
            ans = ans*2 % MOD
        return ans

    def dfs(self, i):
        self.visited[i] = True
        for j in range(len(self.roads[i])):
            if self.roads[i][j] == 'Y' and not self.visited[j]:
                self.dfs(j)


q = [
    ["NYN", "YNN", "NNN"],
    ["NYYY", "YNNN", "YNNN", "YNNN"],
    [
        "NNNNNY",
        "NNNNYN",
        "NNNNYN",
        "NNNNNN",
        "NYYNNN",
        "YNNNNN"
    ]
]

for v in q:
    print(HamiltonPath(v).countPaths())
