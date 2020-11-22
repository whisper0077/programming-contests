r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def one(a, b, c, d):
    if (a+b) == (c+d):
        return True
    if (a-b) == (c-d):
        return True
    if (abs(a-c)+abs(b-d)) <= 3:
        return True
    return False


def two(a, b, c, d):
    if (a+b) % 2 == (c+d) % 2:
        return True
    for dy in range(-3, 3+1):
        for dx in range(-3, 3+1):
            if (abs(dy)+abs(dx)) <= 3 and one(a+dx, b+dy, c, d):
                return True
    return False


def solve(a, b, c, d):
    if a == c and b == d:
        return 0
    if one(a, b, c, d):
        return 1
    if two(a, b, c, d):
        return 2
    return 3


print(solve(r1, c1, r2, c2))
