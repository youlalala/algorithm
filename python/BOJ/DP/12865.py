import sys
input=sys.stdin.readline

n,k=map(int,input().split())

info=[[0,0]]
for _ in range(n):
    info.append(list(map(int,input().split())))
print(info)
dp=[[0]*(k+1) for _ in range(n+1)]

for d in dp:
    print(d)
print()

for i in range(1,n+1):
    for j in range(1,k+1):
        print(i,j)
        w = info[i][0]
        v = info[i][1]
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        for d in dp:
            print(d)
        print()
print(dp[n][k])        

