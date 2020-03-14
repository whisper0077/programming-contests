import math
a, b, c = map(int, input().split())
l = 4*a*b
r = (c-(a+b))*(c-(a+b))
if c < (a+b):
    print("No")
else:
    if l < r:
        print("Yes")
    else:
        print("No")
