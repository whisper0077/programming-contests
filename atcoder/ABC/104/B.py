S = input()
ans = True
ans = ans and S[0] == "A"
ans = ans and S[2:-1].count("C") == 1
ans = ans and S[1:2].islower() and S[-1:].islower()
print(["WA", "AC"][ans])
