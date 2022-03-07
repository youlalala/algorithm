n=int(input())
info=[]
for _ in range(n):
    r,g,b=map(int,input().split())
    info.append([r,g,b])


dp=[[0]*3 for _ in range(n)]

for i in range(n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+info[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+info[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+info[i][2]

print(min(dp[n-1]))

        