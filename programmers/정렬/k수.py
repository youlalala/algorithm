def solution(array, commands):
    answer = []

    
    for i in range(len(commands)):
        a=[]
        b=commands[i]
        a=array[b[0]-1:b[1]]
        a=sorted(a)
        answer.append(a[b[2]-1])
    return answer
