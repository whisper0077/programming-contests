s = input().strip()
p = [['0', '1'], ['1', '0']]
ans = [0, 0]
for i, v in enumerate(s):
    for j in range(2):
        ans[j] = ans[j]+1 if p[j][i % 2] == v else ans[j]
print(min(ans))
