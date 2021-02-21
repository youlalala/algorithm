def solution(arr):
    answer=[]
    
    for idx,ele in enumerate(arr):
        if idx==0:
            answer.append(arr[0])
        else:
            if arr[idx-1]==ele:
                continue
            else:
                answer.append(arr[idx])

    return answer

