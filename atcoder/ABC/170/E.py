import heapq
N, Q = map(int, input().split())
M = 2*10**5+2
rates = [0]*(N+1)
en = [[] for _ in range(M)]
yoji = {}
for n in range(1, N+1):
    A, B = map(int, input().split())
    rates[n] = A
    yoji[n] = B
    heapq.heappush(en[B], [-A, n])

maxs = []
for m in range(1, M):
    if en[m]:
        a, n = en[m][0]
        heapq.heappush(maxs, [-a, n, m])

ans = []
for i in range(Q):
    C, D = map(int, input().split())
    b = yoji[C]
    yoji[C] = D

    # Cをbから移動＆bの最大をmaxsにいれる
    # すでに存在しない幼児は消す
    while en[b]:
        a, n = en[b][0]
        if yoji[n] != b:
            heapq.heappop(en[b])
        else:
            heapq.heappush(maxs, [-a, n, b])
            break

    # CをDに移動＆Dの最大をmaxsに入れる
    # すでに存在しない幼児は消す
    heapq.heappush(en[D], [-rates[C], C])
    while en[D]:
        a, n = en[D][0]
        if yoji[n] != D:
            heapq.heappop(en[D])
        else:
            heapq.heappush(maxs, [-a, n, D])
            break

    # 各園の最大値の中の最小値を表示
    # 記憶している最大値と現在の園の最大値が違う場合は消していく
    while maxs:
        a, n, m = maxs[0]
        if len(en[m]) == 0 or en[m][0][1] != n:
            heapq.heappop(maxs)
        else:
            ans.append(str(a))
            break

print("\n".join(ans))
