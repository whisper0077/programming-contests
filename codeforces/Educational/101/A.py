for t in range(int(input())):
    s = input().strip()
    if len(s) % 2 == 1:
        print("No")
    else:
        if s[0] == ")" or s[-1] == "(":
            print("No")
        else:
            h = {}
            h[0] = True
            n, q = 0, 0
            for v in s:
                nh = {}
                if v == "(":
                    for k in h.keys():
                        nh[k+1] = True
                elif v == ")":
                    for k in h.keys():
                        if k > 0:
                            nh[k-1] = True
                else:
                    for k in h.keys():
                        nh[k+1] = True
                        if k > 0:
                            nh[k-1] = True
                h = nh
            if 0 in h:
                print("Yes")
            else:
                print("No")
