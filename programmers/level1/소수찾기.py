import math
def solution(n):
    r=0
    if n==1:
        return 0
    else:
        for i in range(2,n+1):
            if test(i):
                r+=1             
    return r

def test(x):
    if x<2:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True

print(solution(10))