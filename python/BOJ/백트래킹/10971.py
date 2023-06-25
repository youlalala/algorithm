n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(first,start,cost,visited,cnt):
    global result
    if cnt == n :
        if graph[start][first]:
            cost += graph[start][first]
            if cost <= result :
                result = cost
        return
    
    for k in range(n):
        if graph[start][k] and not visited[k]:
            visited[k] = True
            dfs(first,k,cost+graph[start][k],visited,cnt+1)
            visited[k] = False

#백트래킹
visited = [False] * n
result = 1e9
for i in range(n):
    visited[i] = True
    dfs(i,i,0,visited,1)
    visited[i] = False
print(result)