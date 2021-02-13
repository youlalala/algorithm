import math

def solution(progresses, speeds):
    answer = []

    day=[]
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while(len(day)>=2):
        count=0
        d=day[0]
        day.pop(0)
        print(day)
        count+=1
        while(d>=day[0]):
            day.pop(0)
            print(day)
            count += 1
            if len(day)==0:
                break
        answer.append(count)
    if len(day)==1:
        answer.append(1)          
    return answer

