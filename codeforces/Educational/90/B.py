for t in range(int(input())):
    s = input().strip()
    c = 0
    ok = True
    while ok and len(s) > 0:
        ok = False
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                c += 1
                ok = True
                s = s[:i]+s[i+2:]
                break

    if c % 2 != 0:
        print("DA")
    else:
        print("NET")
