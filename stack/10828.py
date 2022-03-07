import sys
input=sys.stdin.readline

n=int(input())
stk=[]

#정수 X를 스택에 넣는 연산이다.
def push(item):
    stk.append(item)

#스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if (len(stk)==0):
        print(-1)
    else:
        print(stk[-1])
        stk.pop()

#스택에 들어있는 정수의 개수를 출력한다. 
def size():
    print(len(stk))

#스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if (len(stk)==0):
        print(1)
    else:
        print(0)

#스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    if len(stk)==0:
        print(-1)
    else:
        print(stk[-1])

for i in range(n):
    command = input().split()
    if(command[0]=="push"):
        push(int(command[1]))   
    elif(command[0]=="pop"):
        pop()
    elif(command[0]=="size"):
        size()
    elif(command[0]=="empty"):
        empty()
    elif(command[0]=="top"):
        top()