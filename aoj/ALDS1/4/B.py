# 2分探索
n = int(input())
*s, = map(int, input().split())
q = int(input())
*t, = map(int, input().split())

ans = 0
for v in t:
    si, ei = 0, n
    while si < ei:
        mi = (si+ei)//2
        if v == s[mi]:
            ans += 1
            break
        elif v < s[mi]:
            ei = mi
        else:
            si = mi+1

print(ans)
