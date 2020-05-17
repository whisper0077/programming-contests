import math
A, B, H, M = map(int, input().split())
tyousin = M*360/60
tansin = (H*60+M)*360/(12*60)
deg = abs(tyousin-tansin)
if deg >= 180:
    deg = 360-deg

c2 = A*A+B*B-2*A*B*math.cos(math.radians(deg))
print(math.sqrt(c2))
