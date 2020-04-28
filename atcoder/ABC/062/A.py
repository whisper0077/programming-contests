x, y = map(int, input().split())


def group(v):
    if v in [1, 3, 5, 7, 8, 10, 12]:
        return 1
    elif v == 2:
        return 2
    else:
        return 3


if group(x) == group(y):
    print("Yes")
else:
    print("No")
