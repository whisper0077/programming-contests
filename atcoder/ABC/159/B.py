S = input()
N = len(S)


def isP(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if isP(S) and isP(S[:(N-1)//2]) and isP(S[(N+3)//2-1:]):
    print("Yes")
else:
    print("No")
