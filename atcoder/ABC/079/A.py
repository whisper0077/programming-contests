N = input()
ans = "No"
for i in range(10):
    s = str(i)
    if s*3 in N:
        ans = "Yes"
        break
print(ans)
