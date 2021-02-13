# 1번 수포자 1,2,3,4,5 ---
# 2번 수포자 2,1, 2,3, 2,4, 2,5, 2,1,// 2,3 ---
# 3번 수포자 3,3, 1,1, 2,2, 4,4, 5,5,// 3,3, --- 

def solution(answers):
    answer = []
    scores = []
    person1 = [1,2,3,4,5] #5개 반복
    person2 = [2,1,2,3,2,4,2,5] #8개 반복
    person3 = [3,3,1,1,2,2,4,4,5,5] #10개반복
    scores.append(score(answers,person1))
    scores.append(score(answers,person2))
    scores.append(score(answers,person3))
    print(scores,"\n")
    maxscore=max(scores)
    for i in range(len(scores)):
        if scores[i]==maxscore:
            answer.append(i+1)
    print(answer)
    return answer

def score(answers,person):
    score =0
    p=0
    for i in range(len(answers)):
        if (p==len(person)):
            p -= len(person)
        if answers[i] == person[p]:
            score += 1
        p+=1
    return score
solution([1,2,3,4,5])
solution([1,3,2,4,2])