class Neighbors:
    def __init__(self, d):
        self.d = d
        self.n = len(d)
        self.dp = [0]*len(d)

    def maxDonation(self):
        a = self.donation(0, self.n-1)
        self.dp = [0]*self.n
        b = self.donation(1, self.n)
        return max([a, b])

    # メモ化再帰
    def donation(self, n, m):
        if n >= m:
            return 0
        if self.dp[n] > 0:
            return self.dp[n]

        # nを選ぶ
        a = self.d[n] + self.donation(n+2, m)

        # nを選ばない
        b = self.donation(n+1, m)

        r = max([a, b])
        self.dp[n] = r
        return r

    # dp
    def maxDonation2(self):
        ans = 0
        self.dp[0] = self.d[0]
        for i in range(1, self.n-1):
            self.dp[i] = max([self.d[i], self.dp[i-1]])
            if i > 1:
                self.dp[i] = max([self.dp[i], self.dp[i-2]+self.d[i]])
        ans = max(self.dp)

        self.dp[0] = self.d[1]
        for i in range(1, self.n-1):
            self.dp[i] = max([self.d[i+1], self.dp[i-1]])
            if i > 1:
                self.dp[i] = max([self.dp[i], self.dp[i-2]+self.d[i+1]])
        ans = max([ans]+self.dp)
        return ans


q = [
    [10, 3, 2, 5, 7, 8],
    [11, 15],
    [7, 7, 7, 7, 7, 7, 7],
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    [1]*40,
    [i % 10 for i in range(50)]
]
for v in q:
    n, n2 = Neighbors(v), Neighbors(v)
    print(n.maxDonation(), n2.maxDonation2())
