S = input().strip()
d = [0]*10
for s in S:
    d[int(s)] += 1

ans = "No"
if len(S) < 3:
    if len(S) == 1:
        if S == "8":
            ans = "Yes"
    else:
        if int(S) % 8 == 0 or int(S[1]+S[0]) % 8 == 0:
            ans = "Yes"
else:

    for i in range(104, 1000, 8):
        td = [0]*10
        for s in str(i):
            td[int(s)] += 1

        if all([d[i] >= td[i] for i in range(10)]):
            ans = "Yes"
            break

print(ans)
