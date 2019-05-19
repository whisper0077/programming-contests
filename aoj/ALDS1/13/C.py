import copy
import heapq

'''
15パズル
A*アルゴリズム

heapqを使い、マンハッタン距離で評価しながら処理していく
'''

N = 4
N2 = 16


class Puzzle:
    def __init__(self):
        self.space = 0
        self.md = 0
        self.f = [[0 for _ in range(N)] for _ in range(N)]
        self.cost = 0

    def __str__(self):
        return str(self.f)


class State:
    def __init__(self, p):
        self.puzzle = p
        self.est = p.md+p.cost

    def __lt__(self, v):
        return self.est < v.est


mdt = []
for y in range(N2):
    a = []
    for x in range(N2):
        a.append(abs(y//N-x//N)+abs(y % N-x % N))
    mdt.append(a)

pz = Puzzle()
for y in range(N):
    for x, v in enumerate(list(map(int, input().split()))):
        pz.f[y][x] = v
        if v == 0:
            pz.f[y][x] = N2
            pz.space = [y, x]
        else:
            pz.md += mdt[y*N+x][v-1]

st = State(pz)
q = []
heapq.heappush(q, st)
h = {}
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while len(q) > 0:
    st = heapq.heappop(q)
    u = st.puzzle
    if u.md == 0:
        print(u.cost)
        break
    h[str(u)] = True

    sy, sx = u.space
    for dy, dx in d:
        ty, tx = sy+dy, sx+dx
        if ty >= 0 and ty < N and tx >= 0 and tx < N:
            v = copy.deepcopy(u)
            v.md -= mdt[ty*N+tx][v.f[ty][tx]-1]
            v.md += mdt[sy*N+sx][v.f[ty][tx]-1]
            v.f[sy][sx], v.f[ty][tx] = v.f[ty][tx], v.f[sy][sx]
            v.space = [ty, tx]
            if str(v) not in h:
                v.cost += 1
                nst = State(v)
                heapq.heappush(q, nst)
