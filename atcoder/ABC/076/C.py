S = input().strip()
T = input().strip()
ans = "UNRESTORABLE"
for i in range(len(S)-len(T), -1, -1):
    ok = True
    for j in range(len(T)):
        if not (S[i+j] == '?' or S[i+j] == T[j]):
            ok = False

    if ok:
        a = S[:i]+T+S[i+len(T):]
        a = a.replace("?", "a")
        if ans == "UNRESTORABLE" or a < ans:
            ans = a
print(ans)
