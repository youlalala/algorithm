import sys
input = sys.stdin.readline

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m or visited[x][y]:
        return False
    if(graph[x][y]==1):
        visited[x][y]=True
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False

t=int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count=0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if(dfs(i,j)):
                    count+=1
    print(count)
