s = input().strip()
words = ["dream", "dreamer", "erase", "eraser"]
i = len(s)
while i > 0:
    b = False
    for w in words:
        if w == s[i-len(w):i]:
            b = True
            i -= len(w)
            break
    if not b:
        break

print("YES" if i == 0 else "NO")
