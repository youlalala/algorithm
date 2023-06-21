import sys
input = sys.stdin.readline

n,k=map(int,input().split())

coins=[]
for _ in range(n):
    coins.append(int(input()))

dp=[10001]*(k+1)
dp[0]=0

for coin in coins:
    print("coin",coin)
    for i in range(coin, k+1):
        print("i = ",i)
        dp[i]=min(dp[i],dp[i-coin]+1)
        print("dp",dp)
    print()

if(dp[k]==10001):
    print("-1")
else:
    print(dp[k])