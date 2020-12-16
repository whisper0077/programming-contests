A, B = map(int, input().split())
v = [["#"]*100 for _ in range(100)]
for y in range(50):
    for x in range(100):
        v[y][x] = "."

A -= 1
B -= 1

for y in range(0, 50, 2):
    for x in range(0, 100, 2):
        if B > 0:
            v[y][x] = "#"
            B -= 1
        else:
            break

for y in range(51, 100, 2):
    for x in range(0, 100, 2):
        if A > 0:
            v[y][x] = "."
            A -= 1
        else:
            break

print(100, 100)
for y in range(100):
    print("".join(v[y]))
