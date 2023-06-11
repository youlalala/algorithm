# 18352
import sys
from collections import deque

input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int,input().split())

INF = int(1e9)
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n+1)
distance[x] = 0

#BFS
visited = [False] * (n+1)
visited[x] = True
q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] > distance[now] + 1 : 
            q.append(i)
            distance[i] = distance[now] + 1

answer = []
for idx, d in enumerate(distance):
    if d == k:
        answer.append(idx)

if len(answer) == 0 :
    print(-1)
else:
    for a in answer:
        print(a)