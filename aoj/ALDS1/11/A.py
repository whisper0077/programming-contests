n = int(input())
for i in range(n):
    u, k, *v, = map(int, input().split())
    r = []
    for j in range(1, n+1):
        r.append(str(1 if j in v else 0))
    print(" ".join(r))
