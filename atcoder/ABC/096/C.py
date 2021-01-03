h, w = map(int, input().split())
s = []
s.append(["."]*(w+2))
for i in range(h):
    si = input().strip()
    s.append(["."]+list(si)+["."])
s.append(["."]*(w+2))

ans = True
for y in range(1, h+1):
    for x in range(1, w+1):
        if s[y][x] == "#":
            ok = False
            for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if s[y][x] == s[y+dy][x+dx]:
                    ok = True
                    break
            if not ok:
                ans = False
                break

print("Yes" if ans else "No")
