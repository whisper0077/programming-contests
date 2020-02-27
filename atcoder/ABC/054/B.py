N, M = map(int, input().split())
n = [input().strip() for _ in range(N)]
m = [input().strip() for _ in range(M)]

ans = "No"
for y in range(N-M+1):
    for x in range(N-M+1):
        same = True
        for dy in range(M):
            for dx in range(M):
                if n[y+dy][x+dx] != m[dy][dx]:
                    same = False
                    break
            if not same:
                break
        if same:
            ans = "Yes"
            break
print(ans)
