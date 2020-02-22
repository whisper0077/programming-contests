x = int(input())
d = x//11
m = x % 11
ans = d * 2
if m > 6:
    ans += 2
elif m > 0:
    ans += 1
print(ans)
