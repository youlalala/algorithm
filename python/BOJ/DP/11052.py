import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))

dp=[0]*(n+1)
for cardCnt in range(1,n+1):
    print("cardCnt:",cardCnt)
    for k in range(1,cardCnt+1):
        dp[cardCnt] = max(dp[cardCnt], dp[cardCnt-k]+P[k-1])
        print(dp)
print(dp[n])
