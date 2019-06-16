W, H, x, y = map(int, input().split())
s = W*H

ax = W-x
ay = H-y

ok = 0
if ax == x and ay == y:
    ok = 1
print(W*H/2.0, ok)
