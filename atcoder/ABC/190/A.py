a, b, c = map(int, input().split())
ans = "Aoki"
if c == 0:
    if a > b:
        ans = "Takahashi"
else:
    if a >= b:
        ans = "Takahashi"
print(ans)
