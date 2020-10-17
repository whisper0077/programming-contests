X, Y, A, B = map(int, input().split())
e = 0
while (X*A) < (X+B) and (X*A) < Y:
    e += 1
    X *= A

r = Y-X
e += (r-1)//B
print(e)
