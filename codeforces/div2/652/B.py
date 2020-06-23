for t in range(int(input())):
    n = int(input())
    s = input().strip()
    if n == 1:
        print(s)
        continue

    l, r = -1, -1
    for i in range(n):
        if l == -1 and s[i] == "1":
            l = i
        if r == -1 and s[n-i-1] == "0":
            r = i

    if l == -1 or r == -1:
        print(s)
    elif (l+r) == n:
        print(s)
    else:
        print("0"*(l+1)+"1"*r)
