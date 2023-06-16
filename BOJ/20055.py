import sys
input = sys.stdin.readline

n, k = map(int,input().split())
# 내구도
powers = list(map(int,input().split()))
# 로봇 존재 유무
exist = [False] * n

# 단계
step = 0
while True:
    step+=1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    # 로봇 회전
    exist.insert(0,exist.pop())
    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    exist[-1] = False
    # 벨트 회전
    powers.insert(0,powers.pop())

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
    # 만약 이동할 수 없다면 가만히 있는다
    for i in range(n-2,-1,-1):
        if exist[i] == True and exist[i+1] == False:
            if powers[i+1]>=1:
                exist[i+1] = True
                exist[i] = False
                powers[i+1] -= 1
    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    exist[-1] = False
    
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if powers[0]!=0 and exist[0] == False:
        exist[0] = True
        powers[0] -= 1

    # 4. 종료 조건 : 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
    if powers.count(0) >= k:
        break

print(step)