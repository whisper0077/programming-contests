X, Y, Z, K = map(int, input().split())
xyz = []
xyz.append(list(map(int, input().split())))
xyz.append(list(map(int, input().split())))
xyz.append(list(map(int, input().split())))
for v in xyz:
    v.sort()
    v.reverse()

ans = []
for x in range(X):
    for y in range(Y):
        if x*y > K:
            break
        for z in range(Z):
            if x*y*z > K:
                break
            ans.append(xyz[0][x]+xyz[1][y]+xyz[2][z])

ans.sort()
ans.reverse()
print("\n".join([str(v) for v in ans[:K]]))
