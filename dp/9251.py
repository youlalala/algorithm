import sys
input=sys.stdin.readline

stringA=list(input().rstrip())
stringB=list(input().rstrip())

dp=[[0]*(len(stringB)+1) for _ in range(len(stringA)+1)]
for i in range(len(stringA)):
    for j in range(len(stringB)):
        if(stringA[i]==stringB[j]):
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
print(dp[len(stringA)][len(stringB)])

