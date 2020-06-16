T = int(input())
for t in range(T):
    b = input().strip()
    ans = b[:2]
    for i in range(3, len(b), 2):
        ans += b[i]
    print(ans)
