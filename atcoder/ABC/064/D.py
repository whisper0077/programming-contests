N = int(input())
S = input().strip()
l, r = 0, 0
for s in S:
    if s == "(":
        l += 1
    else:
        r += 1
        if l > 0:
            l -= 1
            r -= 1
print("("*r+S+")"*l)
