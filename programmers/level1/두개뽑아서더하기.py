def solution(numbers):
    answer = []

    for idx, ele1 in enumerate(numbers):
        for ele2 in numbers[idx+1:]:
            if ele1+ele2 not in answer:
                answer.append(ele1+ele2)

    answer.sort()
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))