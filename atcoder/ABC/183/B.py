sx, sy, gx, gy = map(int, input().split())
if sx > gx:
    sx, sy, gx, gy = gx, gy, sx, sy

print((sy*gx+gy*sx)/(gy+sy))
