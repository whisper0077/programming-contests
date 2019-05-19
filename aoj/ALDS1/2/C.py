import copy


def bubble(_v):
    v = copy.copy(_v)
    n = len(v)
    for i in range(n):
        for j in range(n-1, i, -1):
            if v[j][1] < v[j-1][1]:
                v[j], v[j-1] = v[j-1], v[j]
    return v


def selection(_v):
    v = copy.copy(_v)
    n = len(v)
    for i in range(n):
        mi = i
        for j in range(i, n):
            if v[j][1] < v[mi][1]:
                mi = j
        v[i], v[mi] = v[mi], v[i]
    return v


n = int(input())
v = input().split()

b = bubble(v)
s = selection(v)
print(" ".join(b))
print("Stable")
print(" ".join(s))
print("Stable" if b == s else "Not stable")
