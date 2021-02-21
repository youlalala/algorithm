def solution(N, stages):

    people=len(stages)
    d=dict()
    for i in range(1,N+1):
        if people==0:
            d[i]=0
            continue

        count=0
        for j in stages:
            if i==j:
                count += 1
        if count==0:
            d[i]=0
        else:
            d[i]=count/people
            people -= count

    d=sorted(d.items(),key=lambda x:x[1], reverse=True)

    print(d)

    
    return [x[0] for x in d]


# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     print(result)
#     return sorted(result, key=lambda x : result[x], reverse=True)

print(solution(5, [1,2,2,1,3]))
