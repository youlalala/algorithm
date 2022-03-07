import sys
input=sys.stdin.readline

def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y]=0
        cnt +=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
                

n=int(input())
graph=[]
for _ in range(n):
    a=list(map(int,input().rstrip()))
    graph.append(a)

result=0
cntlist=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt=0
            if dfs(i,j):
                cntlist.append(cnt)
                result+=1

print(result)
for c in sorted(cntlist):
    print(c)