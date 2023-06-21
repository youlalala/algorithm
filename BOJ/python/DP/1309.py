import sys
input = sys.stdin.readline

n=int(input())

dp = [[1] * 3 for _ in range(n)]
for i in range(1,n):
    #왼쪽에 있는 경우
    dp[i][0]=(dp[i-1][1]+dp[i-1][2]) % 9901
    #오른쪽에 있는 경우
    dp[i][1]=(dp[i - 1][0] + dp[i - 1][2]) % 9901
    #둘다 없는 경우
    dp[i][2]=(dp[i - 1][0]+ dp[i - 1][1] + dp[i - 1][2])%9901
print(dp)
print(sum(dp[n-1])%9901)