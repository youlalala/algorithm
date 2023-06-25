import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
m=int(input())
A.sort()
B=list(map(int,input().split()))

def sort(x,start,end):
    if start>end:
        return False
    mid=(start+end)//2
    if(A[mid]==x):
        return True
    if(A[mid]<x):
        start=mid+1
        return sort(x, start, end)
    elif(A[mid]>x):
        end=mid-1
        return sort(x, start, end)

for b in B:
    #print("num:",b)
    if (sort(b,0,len(A)-1)):
        print("1")
    else:
        print("0")