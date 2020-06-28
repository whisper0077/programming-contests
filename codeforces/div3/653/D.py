from collections import Counter
for t in range(int(input())):
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    b = []
    c = Counter()
    for i in range(n):
        m = k-a[i] % k
        if m < k:
            b.append(m+c[m]*k)
            c[m] += 1
    b.sort()

    x = 0
    for i in range(len(b)):
        if x < b[i]:
            x += b[i]-x+1
        else:
            x += 1

    print(x)
