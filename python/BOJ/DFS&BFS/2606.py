from collections import deque
import sys
input=sys.stdin.readline
def bfs(graph, f,visit):
    count=0
    queue=deque([f])
    visit[f]=True
    while queue:
        v=queue.popleft()   
        for idx, ele in enumerate(graph[v]):
            if ele==1 and not visit[idx]:
                count+=1
                queue.append(idx)
                visit[idx]=True
    return count
n=int(input())
v=int(input())

graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(v):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

visit=[False]*(n+1)
r=bfs(graph, 1, visit)
print(r)

