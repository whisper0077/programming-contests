# 線形検索
n = int(input())
*s, = map(int, input().split())
q = int(input())
*t, = map(int, input().split())

ans = 0
for tt in t:
    for ss in s:
        if ss == tt:
            ans += 1
            break

print(ans)
