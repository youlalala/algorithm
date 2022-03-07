import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
info = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    info[x].append(y)
    info[y].append(x)
for i in info:
    print(i)
print()
visited=[-1]*(n+1)
def bfs(x, y):
    queue = deque()
    queue.append(x)
    visited[x] = 0
    while queue:
        print("queue",queue)
        x= queue.popleft()
        print("x",x)
        if x == y:
            return
        for i in info[x]:
            if (visited[i]==-1):
                queue.append(i)
                visited[i] = visited[x]+1
        print("visited",visited)
bfs(a,b)
print(visited[b])