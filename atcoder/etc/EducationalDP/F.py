import sys
sys.setrecursionlimit(10**8)

s = input().strip()
t = input().strip()
ls = len(s)
lt = len(t)

dp = [[0]*(lt+1) for i in range(ls+1)]

for i in range(ls):
    for j in range(lt):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max([dp[i+1][j], dp[i][j+1]])

ans = ''
i, j = ls, lt
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans = s[i-1]+ans
        i -= 1
        j -= 1

print(ans)
'''
def answer(si, ti):
    if si == ls or ti == lt:
        return ''

    if dp[si][ti] != '':
        return dp[si][ti]

    if s[si] == t[ti]:
        return s[si]+answer(si+1, ti+1)

    a = answer(si+1, ti)
    b = answer(si, ti+1)
    r = a if len(a) > len(b) else b
    dp[si][ti] = r
    return dp[si][ti]


print(answer(0, 0))
'''
