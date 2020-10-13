N = int(input())
txy = [list(map(int, input().split())) for _ in range(N)]
ans = "Yes"
sx, sy = 0, 0
st = 0
for i in range(N):
    t, x, y = txy[i]
    d = abs(sx-x)+abs(sy-y)
    dt = t-st

    if d == dt or (d < dt and (dt-d) % 2 == 0):
        st, sx, sy = t, x, y
    else:
        ans = "No"
        break
print(ans)
