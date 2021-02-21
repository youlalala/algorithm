def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1,arr2):
        r=[]
        for a,b in zip(i,j):
            r.append(a+b)
        answer.append(r)
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]] ))

