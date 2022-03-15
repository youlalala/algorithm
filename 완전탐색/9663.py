import sys
input = sys.stdin.readline
n=int(input())

#줄마다 어느 위치에 놓을지 !
row=[0]*n
#어느 위치 방문??
visited=[False]*n

def check(x):
    for i in range(x):
        if abs(row[x]-row[i]) == x-i :
            return False
    return True


def dfs(x):
    global result
    if(x==n):
        result += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            row[x]=i
            if check(x):
                visited[i]=True
                dfs(x+1)
                visited[i]=False

result=0
dfs(0)
print(result)