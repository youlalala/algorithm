def solution(arr):
    if len(arr)>1:
        rid=sorted(arr)[0]
        arr.remove(rid) 
    else:
        arr=[-1]
    return arr