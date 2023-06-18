import sys
input = sys.stdin.readline

# 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 
# 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 
# 명령의 개수 K (1 ≤ K ≤ 1,000)
n, m, x, y, k = map(int, input().split())

# 지도
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 주사위
dice = [0]*7
current_dice_up = 1

def turn_dice(command, dice):
    a,b,c,d,e,f = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    if command == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = d, b, a, f, e, c
    elif command == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = c, b, f, a, e, d
    elif command == 3 :
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = e, a, c, d, f, b
    elif command == 4:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = b, f, c, d, a, e


comand_info = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
comands = list(map(int,input().split()))
for command in comands:
    nx = x + comand_info[command][0]
    ny = y + comand_info[command][1]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    
    # 주사위 상태 변경
    turn_dice(command, dice)

    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[6]
    else:
        dice[6] = graph[nx][ny]
        graph[nx][ny] = 0

    #  주사위가 이동했을 때 마다 상단에 쓰여 있는 값
    print(dice[1])
    x, y = nx, ny


