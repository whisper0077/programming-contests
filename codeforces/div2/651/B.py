for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    even, odd = [], []
    for i in range(2*n):
        if a[i] % 2 == 0:
            even.append(i+1)
        else:
            odd.append(i+1)

    p = even[:len(even)-len(even) % 2] + odd[:len(odd)-len(odd) % 2]
    for i in range(n-1):
        print(p[i*2], p[i*2+1])
