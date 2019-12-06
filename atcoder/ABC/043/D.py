s = input().strip()
ans = [-1,-1]
if len(s)==2:
    if s[0]==s[1]:
        ans = [1,2]
else:
    for i in range(len(s)-2):
        if len(set(s[i:i+3]))==2:
            ans = [i+1,i+3]
            break
print(ans[0], ans[1])