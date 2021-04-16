N = int(input())
ans = "No"
for i in range(100//4+1):
    for j in range(100//7+1):
        if (4*i+j*7) == N:
            ans = "Yes"
            break
print(ans)
