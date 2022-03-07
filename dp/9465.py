
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    
    n = int(input())
    dp=[]
    for _ in range(2):
        dp.append([0]+list(map(int,input().split())))

    # print("dp",dp)
    # print("check",check)

    for j in range(1,n+1):
        for i in range(2):
            print("i,j",i,j)
            if(j==1):
                continue
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i][j-2],dp[i-1][j-2])+dp[i][j]
            
            for d in dp:
                print(d)
    print(max(dp[1][n],dp[0][n]))
      



