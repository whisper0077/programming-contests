N = int(input())
csf = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    t = csf[i][0]+csf[i][1]
    for j in range(i+1, N-1):
        if t <= csf[j][1]:
            t = csf[j][1]
        else:
            t = (t+csf[j][2]-1)//csf[j][2] * csf[j][2]
        t += csf[j][0]
    print(t)
print(0)
