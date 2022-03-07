import sys
input=sys.stdin.readline

n=int(input())
q=[]

def push(item):
    q.append(item)


def pop():
    if (len(q)==0):
        print(-1)
    else:
        print(q[0])
        q.pop(0)

def size():
    print(len(q))


def empty():
    if (len(q)==0):
        print(1)
    else:
        print(0)


def front():
    if len(q)==0:
        print(-1)
    else:
        print(q[0])

def back():
    if len(q)==0:
        print(-1)
    else:
        print(q[-1])

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
    elif(command[0]=="front"):
        front()
    elif(command[0]=="back"):
        back()
    else:
        exit()