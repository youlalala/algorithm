# 15685
import sys
input = sys.stdin.readline

# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
graph = [ [False]*101 for _ in range(101)]
for _ in range(n):
    # x와 y는 드래곤 커브의 시작 점
    # d는 시작 방향
    # g는 세대
    x, y, d, g = map(int, input().split())

    graph[y][x] = True

    direction_list = [[d]]

    # 세대 돌기
    for i in range(g):
        new_direction_list = []
        # 추가된 방향들을 모두 90도 시계 방향 회전 시킨후 다시 추가
        for directions in direction_list[::-1]:
            for d in directions[::-1]:
                new_direction_list.append((d+1)%4)
        direction_list.append(new_direction_list)
    # print(direction_list)

    for directions in direction_list:
        for i in directions:
            nx = x + dx[i]
            ny = y + dy[i]
            graph[ny][nx] = True
            x, y = nx, ny

# 정사각형 찾기
def find_square():
    answer = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
                answer += 1
    return answer


print(find_square())
