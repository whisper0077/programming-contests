# stack
# 逆ポーランド記法
l = input().split()
s = []
for v in l:
    if v in ["+", "-", "*"]:
        b = s.pop(-1)
        a = s.pop(-1)
        t = eval(a+v+b)
        s.append(str(t))
    else:
        s.append(v)

print(s.pop(0))
