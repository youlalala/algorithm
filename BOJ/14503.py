import sys
input = sys.stdin.readline

# 방 크기
n, m = map(int, input().split())
# 로봇청소기가 있는 칸 좌표 (r,c) / 로봇 청소기가 바라보는 방향 d
r, c, d = map(int, input().split())
# 방향 :  0-북, 1-동, 2-남, 3-서


# 0인 경우 (i, j)가 청소되지 않은 빈 칸이고, 
# 1인 경우 (i, j)에 벽이 있는 것
# -1 - 청소완료
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dirty_cnt(x,y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny] == 0:
            cnt += 1
    return cnt

answer = 0
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if graph[r][c] == 0:
        graph[r][c] = -1
        answer += 1
    
    cnt = dirty_cnt(r,c)
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if cnt == 0:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        nx = r + dx[d]*(-1)
        ny = c + dy[d]*(-1)
        if 0<=nx<n and 0<=ny<m: 
            if graph[nx][ny] == 1:
                break
            else:
                r, c = nx, ny
    else:
        # 반시계 방향으로 90도 회전
        if d == 0:
            d = 3
        else:
            d -= 1
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        nx = r + dx[d]
        ny = c + dy[d]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            r, c = nx, ny
        
print(answer)



