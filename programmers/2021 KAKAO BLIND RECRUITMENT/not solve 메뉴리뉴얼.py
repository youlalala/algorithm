import itertools
def solution(orders, course):
    answer = []
    r=[]
    for i in course:
        com=[]
        for j in orders:
            if len(j) >= i:
                com+=(list(itertools.combinations(j,i)))
        print(i,"개 조합: ",com,"\n")
        
        dic=dict()
        for c in com:
            if c not in dic.keys():
                dic[c] = 1
            else:
                dic[c] += 1
        
        
        for d in dic:
            e=[]
            if dic[d] >=2:
                for i in d:
                    e+=i
                
                r.append(e)

    
    print("r은",r)

    for idx, i in enumerate(r):
        for j in r[(idx+1):]:
            if i in j:
                r.remove(i)

    print("r은",r)

        
    
        



    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])