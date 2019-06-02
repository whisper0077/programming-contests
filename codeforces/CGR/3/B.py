import bisect
n, m, ta, tb, k = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())

ans = -1
for ki in range(k+1):
    if ki < n:
        bi = bisect.bisect_left(b, a[ki] + ta) + k - ki
        if bi < m:
            ans = max(ans, b[bi]+tb)
        else:
            ans = -1
            break
    else:
        ans = -1
        break
print(ans)
