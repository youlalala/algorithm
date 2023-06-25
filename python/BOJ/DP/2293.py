import sys
input = sys.stdin.readline

n,k=map(int,input().split())

coins=[]
for _ in range(n):
    coins.append(int(input()))

dp=[0]*(k+1)
    #for _ in range(n)]
dp[0]=1

for coin in coins:
    print("coin",coin)
    for i in range(coin, k+1):
        print("i = ",i)
        dp[i]+=dp[i-coin]
        print("dp",dp)
    print()

print(dp[k])