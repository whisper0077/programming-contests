s = input().strip()
q = int(input())
l, r = "", ""
rev = 0
for i in range(q):
    a = input().split()
    t = int(a[0])
    if t == 1:
        rev += 1
    else:
        f = int(a[1])
        c = a[2]
        if f == 1:
            if rev % 2 == 0:
                l = c+l
            else:
                r = r+c
        else:
            if rev % 2 == 0:
                r = r+c
            else:
                l = c+l

if rev % 2 == 0:
    print(l+s+r)
else:
    print(r[::-1]+s[::-1]+l[::-1])
