import sys
from collections import  deque
input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

def cal(xlist,ylist):
    visited = [False]*len(xlist)
    queue = deque()
    queue.append((xlist[0],ylist[0]))
    while queue:
        x,y=queue.popleft()
        if abs(x - xlist[-1]) + abs(y - ylist[-1])<=50*20:
            print("happy")
            return
        for i in range(1,len(xlist)):
            nx, ny = xlist[i], ylist[i]
            if (visited[i]==False) and (abs(x - nx) + abs(y - ny)<=50*20):
                queue.append((nx,ny))
                visited[i]=True
    print("sad")

for _ in range(t):
    # 맥주 파는 편의점 수
    n = int(input())
    xlist, ylist = [], []
    # 편의점
    for _ in range(n + 2):
        xx, yy = map(int, input().split())
        xlist.append(xx)
        ylist.append(yy)

    cal(xlist,ylist)
#
#     beer = 20
#     for i in range(0, n + 1):
#         distance = abs(x[i] - x[n+1]) + abs(y[i] - y[n+1])
#         print("distance",distance)
#         if distance<=50*20:
#             if(i==n):
#                 print("happy")
#                 break
#         else:
#             if(i==n):
#                 print("sad")
#                 break
#             else:
#                 continue

