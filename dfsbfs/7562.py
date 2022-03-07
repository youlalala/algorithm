from collections import deque
import sys
input=sys.stdin.readline


def bfs(x, y,move_x,move_y,length):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    while queue:
        x,y=queue.popleft()
        if (x==move_x) and (y==move_y):
            return graph[x][y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<length and 0<=ny<length and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

dx=[1,2,-1,-2,2,1,-1,-2]
dy=[2,1,2,1,-1,-2,-2,-1]

n=int(input())
for i in range(n):
    length=int(input())
    graph = [[0]*length for _ in range(length)]
    now_x,now_y=map(int,input().split())
    move_x, move_y=map(int,input().split())
    print(bfs(now_x,now_y,move_x,move_y,length))
    


