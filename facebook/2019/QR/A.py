t = int(input())
for i in range(t):
    s = input().strip()
    b = s.count('B')
    l = s.count('.')
    ans = 'Y' if b >= l and l > 0 else 'N'
    print(f"Case #{i+1}: {ans}")