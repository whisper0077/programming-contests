
cards = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 9, 10, 11, 12],
    [1, 2, 5, 6, 9, 10, 13, 14],
    [1, 3, 5, 7, 9, 11, 13, 15]
]
abit = 0b111111111111111
bits = []
for c in cards:
    b = 0
    for i in range(len(c)):
        b = b | (1 << (c[i]-1))
    bits.append(b)
    print(bin(b))


def theNumber(answer):
    t = 0b1111111111111111
    for i in range(len(answer)):
        ans = answer[i]
        if ans == "Y":
            t = t & bits[i]
        else:
            t = t & (abit ^ bits[i])
    t = t | 1 << 15
    for i in range(1, 17):
        if t & (1 << (i-1)) > 0:
            return i
    return -1


q = [
    "YNNN",
    "NNNN",
    "YYYY",
    "NYNY"
]

for v in q:
    print(theNumber(v))
