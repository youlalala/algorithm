import sys
input = sys.stdin.readline
T=int(input())

for _ in range(T):
    n = int(input())
    dp = [1] * 101
    if(n>=4):
        for i in range(4,n+1):
            dp[i]=dp[i-3]+dp[i-2]
    print(dp[n])