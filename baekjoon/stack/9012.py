import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    stk=[]
    PS=input().strip()
    for j in range(len(PS)):
        if (len(stk)==0):
            stk.append(PS[j])
        else:
            if (stk[-1]=="(") and (PS[j]==")"):
                stk.pop()

            else:
                stk.append(PS[j])
     

    if (len(stk)==0):
        print("YES")
    else:
        print("NO")