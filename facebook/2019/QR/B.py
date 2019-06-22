t = int(input())
for i in range(t):
    s = input().strip()
    b = s.count('B')
    l = s.count('.')
    ans = 'N'
    if l == 0:
        ans = 'N'
    elif (b - l) >= 0 or b >= 2:
        ans = 'Y'

    print(f"Case #{i+1}: {ans}")