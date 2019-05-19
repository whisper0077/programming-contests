from collections import defaultdict

N = int(input())
MOD = 10**9+7

nglist = [
    "?AGC", "AGC?",
    "A?GC", "AG?C",
    "GAC?", "?GAC",
    "ACG?", "?ACG"
]
ng = {}
for t in "AGCT":
    for n in nglist:
        ng[n.replace('?', t)] = 1

dp = {"TTT": 1}

for i in range(N):
    ans = 0
    _dp = defaultdict(int)
    for k, v in dp.items():
        for t in "AGCT":
            s = k+t
            if s not in ng:
                _dp[s[1:]] += v
                ans = (ans+v) % MOD
    dp = _dp
    if i == (N-1):
        print(ans)
