N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    s = sum([int(v) for v in str(i)])
    if A <= s and s <= B:
        ans += i
print(ans)
