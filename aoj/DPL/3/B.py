H, W = map(int, input().split())
c = []
for _ in range(H):
    *w, = map(int, input().split())
    c.append(w)

'''
最大長方形問題
ヒストグラムの面積を効率的に調べる
'''
# 上方向に連続するタイルの数を記録する
t = []
for _ in range(H+2):
    t.append([0]*(W+2))

for w in range(1, W+1):
    for h in range(1, H+1):
        if c[h-1][w-1] == 1:
            t[h][w] = 0
        else:
            t[h][w] = t[h-1][w]+1

ans = 0
for h in range(1, H+1):
    s = []
    for w in range(1, W+2):
        if len(s) == 0 or s[-1][0] < t[h][w]:
            s.append([t[h][w], w])
        elif s[-1][0] > t[h][w]:
            li = w
            while len(s) > 0 and s[-1][0] >= t[h][w]:
                r = s.pop(-1)
                tmp = (w-r[1])*r[0]
                if tmp > ans:
                    ans = tmp
                li = r[1]
            s.append([t[h][w], li])
print(ans)
