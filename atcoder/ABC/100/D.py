N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            sums = [x*i+y*j+z*k for x, y, z in xyz]
            sums.sort(key=lambda v: -v)
            ans = max(ans, sum(sums[:M]))
print(ans)
