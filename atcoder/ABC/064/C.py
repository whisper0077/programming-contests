N = int(input())
*a, = map(int, input().split())
colors = [0]*8
top = 0
for i in range(N):
    if a[i] < 3200:
        colors[a[i]//400] += 1
    else:
        top += 1

m = 0
for c in colors:
    if c > 0:
        m += 1
print(max(1, m), m+top)
