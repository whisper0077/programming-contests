n = int(input())
*x, = map(int, input().split())
s = sorted(x)
l, r = s[n//2-1], s[n//2]
for i in range(n):
    if x[i] < r:
        print(r)
    else:
        print(l)
