S = list(input().strip())
S.sort()
if "".join(S) == "abc":
    print("Yes")
else:
    print("No")
