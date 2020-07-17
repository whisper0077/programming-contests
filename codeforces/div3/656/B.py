for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    p = [a[0]]
    for i in range(1, 2*n):
        if a[i] not in p:
            p.append(a[i])
    print(*p)
