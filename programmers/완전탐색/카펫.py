def solution(brown, yellow):
    answer = []
    ye=[]
    for i in range(1, yellow+1):
        if (yellow%i==0):
            ye.append(i)
    if len(ye)%2==0:
        for i in ye[:len(ye)//2]:
            ye_row= int(yellow/i)
            ye_col= i
            if (ye_row+2)*(ye_col+2)==brown+yellow:
                answer.append(ye_row+2)
                answer.append(ye_col+2)
    else:
         for i in ye[:len(ye)//2+1]:
            ye_row= int(yellow/i)
            ye_col= i
            if (ye_row+2)*(ye_col+2)==brown+yellow:
                answer.append(ye_row+2)
                answer.append(ye_col+2)       

    print(answer)
    return answer

solution(10,2)
solution(8,1)
solution(24,24)