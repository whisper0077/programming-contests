*v, = map(int, input().split())
v.sort()
ans = 0
for i in range(2):
    while (v[i]+2) <= v[2]:
        v[i] += 2
        ans += 1

odd = 0
for i in range(3):
    if v[i] % 2 == 1:
        odd += 1
v.sort()

if v[0] != v[1] and v[1] == v[2]:
    ans += 2
elif v[0] == v[1] and v[1] != v[2]:
    ans += 1
print(ans)
