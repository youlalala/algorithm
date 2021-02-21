def solution(x):
    a=0
    for i in str(x):
        a+=int(i)
    print(a)
    if x%a !=0:
        return False
    return True

print(solution(11))