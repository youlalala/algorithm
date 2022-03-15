import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
m=int(input())
#시간초과
# for _ in range(m):
#     i,j=map(int,input().split())
#     print(sum(A[i-1:j]))

#누적합
B=[0]*(n+1)
for i in range(1,n+1):
    B[i]=B[i-1]+A[i-1]
#print(B)
for _ in range(m):
    i,j=map(int,input().split())
    print(B[j]-B[i-1])



