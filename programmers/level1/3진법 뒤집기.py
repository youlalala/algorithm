def solution(n):
    a=''
    answer=0
    while(n//3!=0):
        a+=str(n%3)
        n = n//3
    a += str(n)

    for idx, ele in enumerate(a):
        if ele=='0':
            continue
        else:
            answer += int(ele)*(3**(len(a)-idx-1))


    return answer

print(solution(45))
print(solution(125))