H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(list(input().strip()))


for h in range(H):
    for w in range(W):
        x, y = w, h
        if S[y][x] == ".":
            c = 0
            for i in range(max(x-1, 0), min(x+2, W)):
                for j in range(max(y-1, 0), min(y+2, H)):
                    if S[j][i] == "#":
                        c += 1
            S[y][x] = str(c)

for h in range(H):
    print("".join(S[h]))
