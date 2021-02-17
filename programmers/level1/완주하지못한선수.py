def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for idx,ele in enumerate(participant):
        if idx==len(participant)-1:                
            answer=participant[idx]
            break
        elif ele==completion[idx]:
            continue
        elif ele!=completion[idx]:
            answer=ele
            break
    return answer

print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))