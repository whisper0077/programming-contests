A, B = map(int, input().split())
S = input()
s = S.split("-")
ans = "No"
if len(s) == 2 and len(s[0]) == A and len(s[1]) == B:
    t = "".join(s)
    if all([v in "0123456789" for v in t]):
        ans = "Yes"
print(ans)
