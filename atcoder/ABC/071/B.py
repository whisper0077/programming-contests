S = input().strip()
a = [False]*26
for s in S:
    a[ord(s)-ord('a')] = True

ans = "None"
for i in range(len(a)):
    if not a[i]:
        ans = chr(i+ord('a'))
        break
print(ans)
