import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
info = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    info[x].append(y)
    info[y].append(x)
for i in info:
    print(i)
print()
visited=[-1]*(n+1)
visited[a]=0
def dfs(x, y):
    for i in info[x]:
        if (visited[i]==-1):
            visited[i] = visited[x]+1
            print("dfs(",i,y,")")
            dfs(i,y)
dfs(a,b)
print(visited)
print(visited[b])