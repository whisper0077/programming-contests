N = int(input())
*a, = map(int, input().split())
a.sort()
ok = True
t = 1
if N % 2 == 1:
    if a.pop(0) != 0:
        ok = False
    t = 2

if ok:
    for i in range(0, len(a), 2):
        if t != a[i] or t != a[i+1]:
            ok = False
            break
        t += 2

if ok:
    print((2**((N-N % 2)//2)) % (10**9+7))
else:
    print(0)
