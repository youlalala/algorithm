import  sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = int(input())
    dp=[0]*11
    dp[1]=1
    dp[2]=2
    dp[3]=4
    if(num>3):
        for i in range(4,num+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[num])

