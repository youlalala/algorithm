import sys
input = sys.stdin.readline

minute = int(input())
info = []
for _ in range(minute):
    info.append(list(map(int,input().split())))

hw = []
answer = 0
for i in range(minute+1):
    if hw:
        hw[-1][0] -= 1
        if hw[-1][0] == 0:
            answer += hw[-1][1]
            hw.pop()
    if i==minute:
        break
    if len(info[i])!=1:
        _ , a, t = info[i]
        hw.append([t,a])
print(answer)