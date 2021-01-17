X = int(input())
ans = 1
for i in range(2, X+1):
    j = 2
    while pow(i, j) <= X:
        ans = max(ans, pow(i, j))
        j += 1
print(ans)
