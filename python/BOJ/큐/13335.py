import sys
input=sys.stdin.readline

# n : 트럭 수
# w : 다리 길이
# L : 다리 최대 하중
n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w
time = 0
# bridge에 모든 트럭이 지나갈 때 까지 반복
while bridge:
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)