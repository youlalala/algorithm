def solution(dartResult):
    answer = 0
    score=[]
    s=''
    idx=-1
    for i in dartResult:
        if i.isdigit():
            s+=i
        elif i=='S':
            ss=int(s)**1
            score.append(ss)
            idx+=1
            s=''
        elif i=='D':
            ss=int(s)**2
            score.append(ss)
            idx+=1
            s=''
        elif i=='T':
            ss=int(s)**3
            score.append(ss)
            idx+=1
            s=''
        elif i=='*':
            if len(score)==1:
                score[idx] *= 2
            else:
                score[idx-1] *= 2
                score[idx] *= 2
        elif i=='#':
            score[idx ]*= -1

        print("score: ",score)
    for i in score:
        answer += i
            


    return answer
print(solution('1S*2T*3S'))

