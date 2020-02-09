# 0でない数字がちょうどK個
S = input().strip()
K = int(input())
N = len(S)

'''
桁DP
dp[i][j][k] := 
i桁目まで使って
j個の0ではない数値を使って
k=0:i桁目までSと一致
  1:S未満(以下？)
'''
dp = [[[0]*2 for _ in range(K+1)] for _ in range(101)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(K+1):
        for k in range(2):
            nd = int(S[i])
            # 0-9まで調べていく
            for d in range(10):
                ni, nj, nk = i+1, j, k
                if d > 0:
                    nj += 1
                if nj > K:
                    continue
                if k == 0:
                    if d > nd:
                        continue
                    elif d != nd:
                        nk = 1
                dp[ni][nj][nk] += dp[i][j][k]

print(sum(dp[N][K]))

'''
from math import factorial

N = int(input())
K = int(input())


def ncr(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)


def k1(n):
    s = str(n)
    return (len(s) - 1) * 9 + int(s[0])


def k2(n):
    if n < 10:
        return 0
    s = str(n)
    res = ncr(len(s)-1, 2) * 9 * 9
    res += (int(s[0]) - 1) * k1(10 ** (len(s) - 1) - 1) + k1(int(s[1:]))
    return res


def k3(n):
    s = str(n)
    res = ncr(len(s)-1, 3)*9*9*9
    res += (int(s[0]) - 1) * k2(10 ** (len(s) - 1) - 1) + k2(int(s[1:]))
    return res


kf = [k1, k2, k3]
print(kf[K-1](N))
'''
