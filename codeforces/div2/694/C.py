for t in range(int(input())):
    n, m = map(int, input().split())
    *k, = map(int, input().split())
    *c, = map(int, input().split())
    v = [c[i-1] for i in k]
    v.sort(reverse=True)

    vi, ci = 0, 0
    while vi < n and ci < m and v[vi] > c[ci]:
        v[vi] = c[ci]
        vi += 1
        ci += 1

    print(sum(v))
