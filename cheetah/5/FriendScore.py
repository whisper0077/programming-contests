
def highScore(friends):
    ans = 0
    for k in range(len(friends)):
        f = list(friends[k])
        for i in range(len(f)):
            if f[i] == "Y":
                c = friends[i]
                for j in range(len(f)):
                    if k != j and c[j] == "Y":
                        f[j] = "Y"
        t = f.count("Y")
        if t > ans:
            ans = t

    return ans


q = [
    [
        "NNN",
        "NNN",
        "NNN"
    ],
    [
        "NYY",
        "YNY",
        "YYN"
    ],
    [
        "NYNNN",
        "YNYNN",
        "NYNYN",
        "NNYNY",
        "NNNYN"
    ]
]

for v in q:
    print(highScore(v))
