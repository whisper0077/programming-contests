X, A, B = map(int, input().split())
d = B-A
if d <= 0:
    print("delicious")
elif d <= X:
    print("safe")
else:
    print("dangerous")
