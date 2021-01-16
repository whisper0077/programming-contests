H, W = map(int, input().split())
S = "#"*W
ans = 0
for h in range(H):
    s = input().strip()+"#"
    for w in range(W):
        if s[w] == "." and s[w+1] == ".":
            ans += 1
        if s[w] == "." and S[w] == ".":
            ans += 1
    S = s
print(ans)
