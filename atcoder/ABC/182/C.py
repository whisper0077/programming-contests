S = input()
N = int(S)
total = sum([int(s) for s in S])
ans = 20
for i in range(2**len(S)):
    c = total
    t = 0
    for j in range(len(S)):
        if i & (1 << j) != 0:
            c -= int(S[j])
            t += 1
    if c % 3 == 0 and t < len(S):
        ans = min(t, ans)

if ans == 20:
    ans = -1
print(ans)
