a, b = map(int, input().split())
for i in range(1, 1000):
    ta, tb = i*(i+1)//2, (i+1)*(i+2)//2
    if (ta-a) == (tb-b):
        print(ta-a)
        break
