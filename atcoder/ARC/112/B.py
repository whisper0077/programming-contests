def count(r):
    r.sort()
    v = [r[0]]
    for i in range(1, len(r)):
        if r[i][0] <= v[-1][1]:
            v[-1][1] = r[i][1]
        else:
            v.append(r[i])
    return sum([abs(b-a)+1 for a, b in v])


B, C = map(int, input().split())
r = []
if B < 0:
    # マイナス方向
    r.append([B-C//2, B])
    # プラス方向
    r.append([B, B+(C-1)//2])
    # 絶対値の小さい方向を調べる
    if C >= 1:
        C -= 1
        r.append([B-C//2, B])
        r.append([-B, -B+C//2+1-C % 2])
else:
    # プラス方向
    if C >= 2:
        r.append([B, B+(C-2)//2])
    # マイナス方向
    r.append([-B-(C-1)//2, -B])
    # 絶対値の小さい方向を調べる
    r.append([B-C//2, B])
    r.append([-B, -B+(C-1)//2])


print(count(r))
