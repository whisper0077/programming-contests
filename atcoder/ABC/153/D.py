H = int(input())
n = 1
h = H
while True:
    if h == 1:
        break
    n *= 2
    h = h//2

print(n*2-1)
