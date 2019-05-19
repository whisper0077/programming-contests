import copy
p = [list(map(int, input().split())) for _ in range(3)]
sh, sw = 0, 0
ans = copy.deepcopy(p)
for h in range(3):
    for w in range(3):
        ans[h][w] = (h*3+w+1) % 9
        if p[h][w] == 0:
            sh, sw = h, w

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = [[p, [sh, sw], 0]]
c = 0
h = {}
h[str(q[0])] = True
while len(q) > 0:
    t = q.pop(0)
    if t[0] == ans:
        print(t[2])
        break
    for _y, _x in d:
        oy, ox = t[1][0], t[1][1]
        dy, dx = oy+_y, ox+_x
        if dy >= 0 and dy < 3 and dx >= 0 and dx < 3:
            tq = copy.deepcopy(t[0])
            tq[dy][dx], tq[oy][ox] = tq[oy][ox], tq[dy][dx]
            stq = str(tq)
            if stq not in h:
                q.append([tq, [dy, dx], t[2]+1])
                h[stq] = True
