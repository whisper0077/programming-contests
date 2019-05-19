n, k = map(int, input().split())
s = list(input().strip())
s[k - 1] = s[k - 1].lower()
print("".join(s))
