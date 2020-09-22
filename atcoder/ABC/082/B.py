s = input()
t = input()
sd = sorted(s)
td = reversed(sorted(t))
sd = "".join(sd)
td = "".join(td)
if sd < td:
    print("Yes")
else:
    print("No")
