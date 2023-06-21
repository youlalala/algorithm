import heapq as hq
# n개의 도시
n = int(input())
# m개의 버스
m = int(input())

INF = int(1e9)
graph = [ [] for _ in range(n+1)]
reverse_graph = [ [] for _ in range(n+1)]
for _ in range(m):
    # a~b 까지 가는 비용 c
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a,c))

# 출발점, 도착점
start, end = map(int,input().split())

# 최단거리 찾기
distance = [INF] * (n+1)
def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dis , node = hq.heappop(q)
        if dis > distance[node]:
            continue
        for idx, cost in graph[node]:
            if dis + cost < distance[idx]:
                distance[idx] = dis+cost
                hq.heappush(q,(distance[idx], idx))
                
dijkstra(start)

# 경로 찾기
route = [end]
current = end
while current != start:
    for idx, cost in reverse_graph[current]:
        if distance[current] - cost == distance[idx]:
            route.append(idx)
            current = idx
            break


# 최소비용, 거치는 도시 개수, 도시 순서 대로 출력
print(distance[end])
print(len(route))
print(' '.join(map(str, route[::-1])))
