V, E, r = map(int, input().split())
inf = 2**32
e = []
for i in range(E):
    s, t, d = map(int, input().split())
    e.append([s, t, d])

# 始点からの距離初期化
distance = [inf]*V
distance[r] = 0

'''
ベルマンフォード法による単一最短経路
負の重みがある場合でも大丈夫だが、負の重みがない場合はダイクストラのほうがよい
O(V*E)
'''


def bellmanFord():
    for v in range(V):
        updated = False
        for s, t, d in e:
            if distance[s] != inf and (distance[s]+d) < distance[t]:
                distance[t] = distance[s]+d
                updated = True
        if v == (V-1) and updated:
            return False
    return True


b = bellmanFord()
if b:
    for v in range(V):
        print(distance[v] if distance[v] != inf else "INF")
else:
    print("NEGATIVE CYCLE")
