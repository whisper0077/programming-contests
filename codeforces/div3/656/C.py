for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    m = 0
    i = n
    while i > 0 and m <= a[i-1]:
        m = a[i-1]
        i -= 1
    while i > 0 and m >= a[i-1]:
        m = a[i-1]
        i -= 1
    print(i)
