import sys
input = sys.stdin.readline

n = int(input())

def is_promising(cnt):
    for k in range(cnt):
        # 가로 세로
        if location[k] == location[cnt]:
            return False
        # 대각선
        elif abs(k-cnt) == abs(location[k]-location[cnt]):
            return False
    return True


location = [0] * n
def n_queen(cnt):
    global answer
    if cnt == n:
        answer += 1
        return 
    for i in range(n):
        location[cnt] = i 
        if is_promising(cnt):
            n_queen(cnt+1)


answer = 0
n_queen(0)
print(answer)