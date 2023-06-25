
from collections import deque
import math
import sys
input = sys.stdin.readline
# 서로 맞닿은 톱니의 극이 다르다면, 반대 방향
# 극이 같다면, 안움직임


# N극은 0, S극은 1
a = deque(list(map(int,input().strip())))
b = deque(list(map(int,input().strip())))
c = deque(list(map(int,input().strip())))
d = deque(list(map(int,input().strip())))
ns_list = [a,b,c,d]

k = int(input())
for _ in range(k):
    # wheel_direction : 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
    # wheel_num : 1,2,3,4
    wheel_num, wheel_direction = map(int, input().split())

    dircetion_list = [0,0,0,0]
    dircetion_list[wheel_num-1] = wheel_direction

    # 오른쪽 바퀴들 체크
    compare_ns = ns_list[wheel_num-1][2]
    for i in range(wheel_num,4):
        # 왼쪽 맞닿은 부분
        if compare_ns != ns_list[i][6]:
            dircetion_list[i] = dircetion_list[i-1]*(-1)
        compare_ns = ns_list[i][2]

    # 왼쪽 바퀴들 체크
    compare_ns = ns_list[wheel_num-1][6]
    for i in range(wheel_num-2,-1,-1):
        # 오른쪽쪽 맞닿은 부분
        if compare_ns != ns_list[i][2]:
            dircetion_list[i] = dircetion_list[i+1]*(-1)
        compare_ns = ns_list[i][6]

    for i in range(4):
        if dircetion_list[i] == 1:
            ns_list[i].rotate(1)
        elif dircetion_list[i] == -1:
            ns_list[i].rotate(-1)

answer = 0
for i in range(4):
    if ns_list[i][0] == 1 :
        answer += math.pow(2,i)
print(int(answer))