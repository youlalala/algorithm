import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 주변의 물 세기
def count_water(x,y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            count += 1
    return count

# 덩어리 갯수 찾기
def dfs(x,y):
    global visited, graph
    if x>=n or y>=m or x<0 or y<0 :
        return False
    if graph[x][y] <= 0:
        return False
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False
    

year = 0
while True:
    visited = [ [False] * m for _ in range(n) ]
    
    # 빙하 덩어리 찾기
    ice = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                ice += 1

    # 덩어리 수가 2 보다 많으면 break
    if ice > 1:
        break
    elif ice == 0 : 
        year = 0
        break

    # 2보다 적으면 주변 물 세기
    water_graph = [ [0] * m for _ in range(n) ]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                water_graph[i][j] = count_water(i,j)


    # 1년 후 빙하가 녹는다.
    year += 1
    for i in range(n):
        for j in range(m):
            cnt = water_graph[i][j]
            if graph[i][j] >= cnt:
                    graph[i][j] -= cnt
            else:
                graph[i][j] = 0    
    
print(year)