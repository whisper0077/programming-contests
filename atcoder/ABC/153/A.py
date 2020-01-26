H, A = map(int, input().split())
a = H//A
if H % A > 0:
    a += 1
print(a)
