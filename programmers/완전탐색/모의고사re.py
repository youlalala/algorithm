# 1번 수포자 1,2,3,4,5 ---
# 2번 수포자 2,1, 2,3, 2,4, 2,5, 2,1,// 2,3 ---
# 3번 수포자 3,3, 1,1, 2,2, 4,4, 5,5,// 3,3, --- 

def solution(answers):
    answer = []
    scores = [0,0,0]
    person1 = [1,2,3,4,5] #5개 반복
    person2 = [2,1,2,3,2,4,2,5] #8개 반복
    person3 = [3,3,1,1,2,2,4,4,5,5] #10개반복

    for i,a in enumerate(answers):
        if a==person1[i%len(person1)]:
            scores[0] += 1
        if a==person2[i%len(person2)]:
            scores[1] += 1
        if a==person3[i%len(person3)]:
            scores[2] += 1

    for i, s in enumerate(scores):
        if s == max(scores):
            answer.append(i+1)
            

    return answer

