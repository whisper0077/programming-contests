
class Salary:
    def __init__(self, r):
        self.r = r
        self.dp = [0]*len(r)

    def totalSalary(self):
        s = 0
        for i in range(len(self.r)):
            s += self.getSalary(i)
        return s

    def getSalary(self, n):
        if self.dp[n] > 0:
            return self.dp[n]
        s = 0
        for i in range(len(self.r[n])):
            if self.r[n][i] == 'Y':
                s += self.getSalary(i)
        s = max([1, s])
        self.dp[n] = s
        return s


q = [
    ["N"],
    ["NNYN", "NNYN", "NNNN", "NYYN"],
    [
        "NNNNNN",
        "YNYNNY",
        "YNNNNY",
        "NNNNNN",
        "YNYNNN",
        "YNNYNN"
    ]
]
for v in q:
    s = Salary(v)
    print(s.totalSalary())
