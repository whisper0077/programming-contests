import fractions


def gcd(l, t):
    a = l.pop(0)
    for v in l:
        a = fractions.gcd(a, v)
        if a <= t:
            break
    return a


N = int(input())
*A, = map(int, input().split())
A.sort()

dp = [[1]*N for i in range(2)]
dp[0][0] = A[0]

a, b = A[0], A[-1]
for i in range(1, N):
    a = fractions.gcd(a, A[i])
    dp[0][i] = a
    b = fractions.gcd(b, A[N-i])
    dp[1][N-i] = b

ans = 1
for i in range(N):
    g = 1
    if i == 0:
        g = dp[1][1]
    elif i == (N-1):
        g = dp[0][-2]
    else:
        g = fractions.gcd(dp[0][i-1], dp[1][i+1])
    if g > ans:
        ans = g
print(ans)
