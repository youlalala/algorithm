import sys
input=sys.stdin.readline


while True:
    ex=input().rstrip()
    stk=[]
    if ex=='.':
        break
    for i in ex:     
        if i.isalpha():
            continue
        elif (i=="(" or i=="["):
            stk.append(i)
        elif (i==")" or i=="]")  and len(stk)==0:
            break        
        elif i==")" and stk[-1]=="(":
            stk.pop()
        elif i=="]" and stk[-1]=="[":
            stk.pop()


    if len(stk)==0:
        print("yes")
    else:
        print("no")