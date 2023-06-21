# 빌딩 수 
n = int(input())
INF = int(1e9)
buildings = list(map(int, input().split()))
answer = [0]*n

for i in range(n):
    # 오른쪽 체크
    right_max_gradient = -INF
    for j in range(i+1,n):
        gradient =(buildings[j]-buildings[i])/(j-i)
        if right_max_gradient < gradient:
            right_max_gradient = gradient
            answer[i] += 1

    # 왼쪽 체크
    left_max_gradient = INF
    for j in range(i-1,-1,-1):
        gradient =(buildings[i]-buildings[j])/(i-j)
        if left_max_gradient > gradient:
            left_max_gradient = gradient
            answer[i] += 1
print(max(answer))