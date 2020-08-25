for t in range(int(input())):
    s = input()
    x = int(input())
    n = len(s)
    w = ["1"]*n

    for i in range(n):
        if s[i] == "0":
            if i >= x:
                w[i-x] = "0"
            if (i+x) < n:
                w[i+x] = "0"

    for i in range(n):
        if s[i] == "1":
            wi = "0"
            if i >= x and w[i-x] == "1":
                wi = "1"
            if (i+x) < n and w[i+x] == "1":
                wi = "1"
            if wi != "1":
                w = ["-1"]
                break
    print("".join(w))
