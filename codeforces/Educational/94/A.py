for t in range(int(input())):
    n = int(input())
    s = input()
    one, zero = 0, 0
    for i in range(2*n-1):
        if s[i] == "0":
            zero += 1
        if s[i] == "1":
            one += 1
    if one > zero:
        print("1"*n)
    else:
        print("0"*n)
