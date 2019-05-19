a = [int(input()) for _ in range(5)]
ans = 1000


def solve(l, t):
    global ans
    if len(l) == 0:
        if ans > t:
            ans = t
        return
    if t % 10 > 0:
        t = t+10-t % 10
    for i, v in enumerate(l):
        solve(l[:i]+l[i+1:], t+l[i])


solve(a, 0)
print(ans)
