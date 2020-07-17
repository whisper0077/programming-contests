

def dfs(n, s, c):
    if len(s) <= 1:
        return 0 if s[0] == c else 1

    l = n//2-s[:n//2].count(c) + dfs(n//2, s[n//2:], chr(ord(c)+1))
    r = dfs(n//2, s[:n//2], chr(ord(c)+1)) + n//2-s[n//2:].count(c)
    return min(l, r)


for t in range(int(input())):
    n = int(input())
    s = input().strip()
    print(dfs(n, s, 'a'))
