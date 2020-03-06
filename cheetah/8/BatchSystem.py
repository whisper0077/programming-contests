from collections import defaultdict


def schedule(durations, users):
    h = defaultdict(int)
    for i in range(len(users)):
        h[users[i]] += durations[i]

    ans = []
    while len(h) > 0:
        user = None
        for i in range(len(users)):
            if users[i] in h and (user == None or (h[users[i]] < h[user])):
                user = users[i]
        for i in range(len(users)):
            if users[i] == user:
                ans.append(i)
        del(h[user])
    return ans


q = [
    [
        [400, 100, 100, 100],
        ["D", "S", "S", "M"]
    ]
]

for v in q:
    print(schedule(*v))
