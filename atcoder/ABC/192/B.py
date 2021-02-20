S = input().strip()
ans = "Yes"
for i in range(len(S)):
    if i % 2 == 0:
        if ord(S[i]) < ord("a"):
            ans = "No"
            break
    else:
        if ord(S[i]) >= ord("a"):
            ans = "No"
            break
print(ans)
