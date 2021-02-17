def solution(n, lost, reserve): 
    #여벌 체육복을 가져왔는데 도난 당한 경우
    reservelist = set(reserve)-set(lost) 
    lostlist = set(lost)-set(reserve) 

    for i in reservelist: 
        if i-1 in lostlist: 
            lostlist.remove(i-1) 
        elif i+1 in lostlist: 
            lostlist.remove(i+1) 
    return n-len(lostlist)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(5,[2,4],[2,3,4]))