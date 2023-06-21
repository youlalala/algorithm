import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,deep):
    #안전하지않은 영역
    if(1<tmpgraph[x][y]<=deep):
        return False
    if(tmpgraph[x][y]>deep):
        tmpgraph[x][y] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            else:
                dfs(nx,ny,deep)
        return True
    return False

result=0
deep=0
cnt=100
while(cnt!=0 and deep<=100):
    tmpgraph=[]
    for row in range(n):
        tmpgraph.append(graph[row][:])
    cnt=0
    for i in range(n):
        for j in range(n):
            if(tmpgraph[i][j]>deep):
                if(dfs(i,j,deep)):
                    cnt+=1
    result=max(result,cnt)
    deep+=1
print(result)