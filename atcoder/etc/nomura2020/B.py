T = list("X"+input())
for i in range(1, len(T)):
    if T[i] == "?":
        T[i] = "D"

print("".join(T[1:]))
