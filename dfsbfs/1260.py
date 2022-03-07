import collections
import sys
input=sys.stdin.readline

def dfs(graph,f,visit):
    visit[f]=True
    print(f, end=' ')
    for idx, ele in enumerate(graph[f]):
        if ele==1 and not visit[idx]:
            dfs(graph,idx,visit)


def bfs(graph,f,visit):
    queue=collections.deque([f])
    visit[f]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for idx, ele in enumerate(graph[v]):
            if ele==1 and not visit[idx]:
                queue.append(idx)
                visit[idx]=True

n,v,first=map(int, input().split())
graph=[[0]*(n+1) for i in range(n+1)]
visit=[False]*(n+1)
for i in range(v):
    a,b=map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(graph,first,visit)
visit=[False]*(n+1)
print()
bfs(graph,first,visit)


    








