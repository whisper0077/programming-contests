sx, sy, tx, ty = map(int, input().split())
dx, dy = tx-sx, ty-sy
ans = ""
ans += dy*"U" + dx*"R"
ans += dy*"D" + dx*"L"
ans += "L" + (dy+1)*"U" + (dx+1)*"R" + "D"
ans += "R" + (dy+1)*"D" + (dx+1)*"L" + "U"
print(ans)
# UURDDLLUUURRDRDDDLLU
# UURDDLLUUURRDRDDDLLU
