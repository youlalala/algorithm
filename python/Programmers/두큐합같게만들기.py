# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    max_cnt = (len(queue1)+len(queue2))*2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 시간초과 원인
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    answer = 0
    while sum1 != sum2:
        if sum1 >= sum2:
            element = queue1.popleft()
            queue2.append(element)
            answer += 1
            sum1 -= element
            sum2 += element
        else:
            element = queue2.popleft()
            queue1.append(element)
            answer += 1
            sum2 -= element
            sum1 += element
        if answer > max_cnt:
            answer = -1
            break
    
    return answer