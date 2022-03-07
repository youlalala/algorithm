import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    g = [int(num) for num in input().strip()]
    graph.append(g)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, count):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    while (queue):
        count += 1
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx == n or ny < 0 or ny == m:
                continue
            elif graph[nx][ny] == 0 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return count


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j]=bfs(i, j, 0)


for gr in graph:
    for i in gr:
        print(i,end='')
    print()