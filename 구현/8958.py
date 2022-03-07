import sys
input = sys.stdin.readline

n=int(input())
for _ in range(n):
    oxList=[ox for ox in input()]
    result=0
    score=0
    for item in oxList:
        if(item=='O'):
            score+=1
            result += score
        else:
            score=0
    print(result)