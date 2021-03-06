a, b = map(int, input().split())
k = a+b
s = b
if k >= 15 and s >= 8:
    print(1)
elif k >= 10 and s >= 3:
    print(2)
elif k >= 3:
    print(3)
else:
    print(4)
