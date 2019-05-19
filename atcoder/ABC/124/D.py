N, K = map(int, input().split())
s = input().strip()
sb, eb = False, False
if s[0] == '0':
    s = '1'+s
    sb = True
if s[-1] == '0':
    s = s+'1'
    eb = True
i = 0
dp = []
while i < len(s):
    l = i
    while i < len(s) and s[i] == '1':
        i += 1
    if l < i:
        dp.append([l, i-1])
    while i < len(s) and s[i] == '0':
        i += 1


if len(dp) <= K:
    print(N)
else:
    ans = 0
    for i in range(0, len(dp)-K):
        t = dp[i+K][1]-dp[i][0]+1
        if t > ans:
            ans = t
            if (sb and i == 0) or (eb and i == (len(dp)-K-1)):
                ans -= 1
    print(ans)
