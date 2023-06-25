import sys
input=sys.stdin.readline

n=int(input())
coins=[500,100,50,10,5,1]
change=1000-n
count=0
for coin in coins:
    a=change//coin
    b=change%coin
    if a>0:
        count+=a
        change-=a*coin
    
print(count)