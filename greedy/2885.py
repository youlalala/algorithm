import sys
input=sys.stdin.readline

# n : 초콜릿 1개에 정사각형 n개
# 초콜릿 크기 = 정사각형 갯수 : 2 의 제곱
# K 개의 정사각형을 먹어야 버팀

chocolate_size = 1
k = int(input())
while True:
    if k <= chocolate_size :
        break
    chocolate_size *= 2

cut_cnt = 0
cut_size = chocolate_size
get_size = chocolate_size
while True:
    if get_size == k:
        break
    elif get_size < k:
        cut_cnt += 1
        cut_size /= 2
        get_size += cut_size
    else:
        cut_cnt += 1
        cut_size /= 2
        get_size -= cut_size

print(chocolate_size, cut_cnt)