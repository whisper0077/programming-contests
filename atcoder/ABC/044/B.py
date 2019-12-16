import collections
s = list(input())
d = collections.Counter(s)
ans = "Yes"
for v in d.values():
    if v%2==1:
        ans="No"
        break
print(ans)