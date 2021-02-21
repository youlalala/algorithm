import math
def solution(n):
    r=math.sqrt(n)
    if str(r)[-2:]==".0":
        return (r+1)**2
    else:
        return -1