import sys
input = sys.stdin.readline

n=int(input())
cards=list(map(int,input().split()))
cards.sort()
m=int(input())

def find(num,start,end):
    # print("num:",num,"\nstart,end",start,end)
    while(start!=end):
        mid = (start + end) // 2
        if num==cards[mid]:
            return True
        elif num<cards[mid]:
            end=mid
        elif num>cards[mid]:
            start=mid+1
    return False

length=len(cards)
for num in list(map(int,input().split())):
    if find(num,0,length):
        print("1 ",end='')
    else:
        print("0 ",end='')