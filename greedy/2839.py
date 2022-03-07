import sys
input=sys.stdin.readline

n=int(input())

li=[5,3]
cnt=0
for i in li:
    a=n//i
    while(a>0 and (n-a*i)%3!=0):
        a-=1
    if a>0 and (n-a*i)%3==0:
        cnt+=a
        n-=a*i
        continue

if n==0:
    print(cnt)
else:
    print(-1)