N = int(input())
ba = []
for i in range(N):
    a, b = map(int, input().split())
    ba.append([b, a])
ba.sort()

ans = "Yes"
c = 0
for i, v in enumerate(ba):
    b, a = v
    c += a
    if c > b:
        ans = "No"
        break
print(ans)
