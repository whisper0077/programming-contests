def xXtry(s):
    x, X = 1, 0
    a = eval(s)
    x, X = X, x
    b = eval(s)
    if a == b:
        return str(a)
    else:
        return 'x' if a == 1 else 'X'


T = int(input())
for t in range(T):
    s = input().strip()
    ans = 0
    if len(s) == 1:
        if s in ["x", "X"]:
            ans = 1
    else:
        while len(s) > 1:
            ns = ""
            i = 0
            while i < len(s):
                if s[i] == '(' and s[i + 4] == ')':
                    ns += xXtry(s[i + 1:i + 4])
                    i += 5
                else:
                    ns += s[i]
                    i += 1
            if len(ns) == len(s):
                break
            s = ns
        if s in ["x", "X"]:
            ans = 1

    print(f"Case #{t+1}: {ans}")