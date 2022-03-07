from collections import deque
import sys
input=sys.stdin.readline

dx = [-1, 1, 0, 0,1,-1,1,-1]
dy = [0, 0, -1, 1,1,-1,-1,1]


def dfs(x,y):
    if 0 <= x < h and 0 <= y < w and graph[x][y] == 1:
        graph[x][y]=0
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

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
            if(dfs(i,j)==True):
                result+=1
    print(result)
