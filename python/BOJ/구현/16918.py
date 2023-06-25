r, c, n = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            graph[i][j] = 0
        elif graph[i][j] == '.':
            graph[i][j] = -1


def bomb(bomb_location):
    for x, y in bomb_location:
        graph[x][y] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            else:
                graph[nx][ny] = 0


bombPlay = False
for second in range(1, n + 1):
    bomb_location = []
    if bombPlay:
        for i in range(r):
            for j in range(c):
                graph[i][j] += 1
        bombPlay = False

    else:
        for i in range(r):
            for j in range(c):
                if graph[i][j] >= 2:
                    bomb_location.append((i, j))
                else:
                    graph[i][j] += 1

        bomb(bomb_location)
        bombPlay = True

for i in range(r):
    for j in range(c):
        if graph[i][j] != 0:
            graph[i][j] = 'O'
        else:
            graph[i][j] = '.'
    print(''.join(graph[i]))
