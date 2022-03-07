import sys
input=sys.stdin.readline

n,k= map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))

cnt=0
for coin in reversed(coins):
    a=k//coin
    b=k%coin
    if k//coin>0:
        cnt += a
        k -= coin*a
    if k==0:
        print(cnt)
        break