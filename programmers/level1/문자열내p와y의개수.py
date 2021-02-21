def solution(s):
    pcount=0
    ycount=0
    s=s.lower()
    for i in s:
        if i=="p":
            pcount +=1
        elif i=="y":
            ycount +=1
    
    if pcount != ycount:
        return False

    return True