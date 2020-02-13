N = int(input())
S = input()
ans = 0
t = 0
for s in S:
    if s == 'I':
        t += 1
        if t > ans:
            ans = t
    else:
        t -= 1
print(ans)
