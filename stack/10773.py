import sys
input=sys.stdin.readline

n=int(input())
stk=[]
for i in range(n):
    num=int(input())
    if num==0:
        if len(stk)==0:
            stk.append(num)
        else:
            stk.pop()
    else:
        stk.append(num)

answer=0
for s in stk:
    answer +=s
print(answer)