import sys
input=sys.stdin.readline

num=int(input())
times=list(map(int,input().split()))
times.sort()
maxnum=len(times)
sum = 0
for i,j in zip(times,range(maxnum,0,-1)):
    sum += i*j
print(sum)