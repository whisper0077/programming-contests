
def find(s):
    ans = 0
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            ans += 1
            i += 1
        else:
            i += 1
            j -= 1
    return ans+len(s)


q = [
    "abab",
    "abvba",
    "qwerty"
]

for v in q:
    print(v, find(v))
