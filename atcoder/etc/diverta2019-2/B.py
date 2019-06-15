N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort()

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        p = xy[j][0]-xy[i][0]
        q = xy[j][1]-xy[i][1]
        merge = 0
        for k in range(N):
            if [xy[k][0]+p, xy[k][1]+q] in xy:
                merge += 1
        ans = max(ans, merge)
print(N-ans)
