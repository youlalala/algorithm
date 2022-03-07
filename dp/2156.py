
import sys
input=sys.stdin.readline
n=int(input())
graph=[]
for _ in range(n):
    graph.append(int(input()))

# print(graph)
dp=[[0]*(n) for _ in range(3)]
# print(dp)
for i in range(n):
    for j in range(3):
        #print("i,j",i,j)
        if(j==1 and 0<=i<=1):
            dp[j][i]=graph[i]
        elif(i==0 and (j==0 or j==2)):
            dp[j][i]=0
        elif(j==0):
            dp[j][i]=max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
        else:
            dp[j][i]=dp[j-1][i-1]+graph[i]
        for d in dp:
            print(d)
        print()
print(max(max(dp[0]),max(dp[1]),max(dp[2])))
    