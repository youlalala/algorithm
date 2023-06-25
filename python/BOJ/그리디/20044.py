import sys
input=sys.stdin.readline

# 학생수 : 2n
# 코딩 역량 : w
# Gi 한 팀의 코딩 역량 w(Gi)
# Sm 이 최대화 되도록 구성

n = int(input())
list = list(map(int, input().split()))
list.sort()

sum_list = []
for i in range(n):
    sum_result = 0
    sum_result = list[i] + list[2*n-i-1]
    sum_list.append(sum_result)

print(min(sum_list))