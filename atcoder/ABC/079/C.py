def solve():
    a, b, c, d = map(int, list(input()))
    op = ["+", "-"]
    ans = ""
    for op1 in range(2):
        for op2 in range(2):
            for op3 in range(2):
                s = "a"+op[op1]+"b"+op[op2]+"c"+op[op3]+"d"
                if eval(s) == 7:
                    return str(a)+op[op1]+str(b)+op[op2]+str(c)+op[op3]+str(d)+"=7"


print(solve())
