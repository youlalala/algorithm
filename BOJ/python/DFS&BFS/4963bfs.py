from collections import deque
import sys
input=sys.stdin.readline

dx = [-1, 1, 0, 0,1,-1,1,-1]
dy = [0, 0, -1, 1,1,-1,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y]= 0
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    return True

while(True):
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    graph=[]
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    result=0
    for i in range(h):
        for j in range(w):
            if(graph[i][j]==1):
                bfs(i,j)
                result+=1
    print(result)
