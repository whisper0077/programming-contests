from collections import Counter
T = int(input())
for t in range(T):
    s = list(input())
    m = int(input())
    *b, = map(int, input().split())
    ans = [""]*m

    s.sort()
    s.reverse()

    cnt = Counter(s)

    prev = ""
    for c in s:
        if prev == c:
            continue

        ids = []
        for i in range(m):
            if ans[i] == "" and b[i] == 0:
                ids.append(i)

        if len(ids) <= cnt[c]:
            for i in ids:
                ans[i] = c
                for j in range(m):
                    b[j] -= abs(i-j)

        prev = c
    print("".join(ans))
