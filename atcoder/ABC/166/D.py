
X = int(input())
for a in range(-120, 120):
    find = False
    for b in range(-120, 120):
        x = a**5-b**5
        if x == X:
            find = True
            print(a, b)
            break
    if find:
        break
