n = int(input())
*a, = map(int, input().split())
ao, ae = 0, 0
for i, v in enumerate(a):
    if v % 2 == 0:
        ae += 1
    else:
        ao += 1
if ao > 0 and ae > 0:
    a.sort()

print(" ".join([str(v) for v in a]))