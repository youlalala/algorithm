import sys
input = sys.stdin.readline

n=int(input())
scoreList=[0]
for _ in range(n):
    scoreList.append(int(input()))

dp=[0]*(n+1)
if(n==1):
    print(scoreList[1])
else:
    dp[1] = scoreList[1]
    dp[2]= scoreList[1]+scoreList[2]
    for i in range(3,n+1):
        dp[i]=max(dp[i-3]+scoreList[i-1]+scoreList[i], dp[i-2]+scoreList[i])
    print(dp[n])
# dp=[[0]*3 for _ in range(n)]

#
# dp[0][1]=scoreList[0]

# for i in range(1,n):
#     for j in range(3):
#         if j==0:
#             dp[i][j]=max(dp[i-1])
#         else:
#             dp[i][j]=dp[i-1][j-1]+scoreList[i]
#     print(dp)

# print(max(dp[n-1][1],dp[n-1][2]))

