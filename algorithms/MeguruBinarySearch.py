def isOk1(i, a, b):
    if i < 0:
        return True
    if i >= len(a):
        return False
    return a[i] < b


def isOk2(i, a, b):
    if i < 0:
        return False
    if i >= len(a):
        return True
    return a[i] > b


# ok<ng 条件を満たす中で最大のindexを返す
# ok>ng 条件を満たす中で最小のindexを返す
def MeguruSearch(a, v, _ok, _ng, _isOk):
    ok, ng = _ok, _ng
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if _isOk(mid, a, v):
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    a = [1, 3, 3, 4, 7, 10, 11, 20]
    print(MeguruSearch(a, 4, 0, len(a), isOk1))
    print(MeguruSearch(a, 4, len(a), 0, isOk2))
