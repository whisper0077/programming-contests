N = int(input())
a = [0]*(N+1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            d = x*x+y*y+z*z+x*y+y*z+x*z
            if d <= N:
                a[d] += 1
for i in range(1, N+1):
    print(a[i])
