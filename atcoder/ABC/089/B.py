N = int(input())
S = input().split()
c = set()
for s in S:
    c.add(s)

if len(c) == 3:
    print("Three")
else:
    print("Four")
