import sys
input = sys.stdin.readline

INF = int(1e9)
test_case_num = 0
while True:
    n = int(input())
    if n == 0:
        break

    test_case_num += 1
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    dp = [ [0]*3 for _ in range(n)]
    dp[0][0] = INF
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1]+graph[0][2]
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][0],dp[i-1][1]) + graph[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][1],dp[i-1][2],dp[i][0])+ graph[i][1]
        dp[i][2] = min(dp[i-1][1],dp[i-1][2],dp[i][1]) + graph[i][2]
    
    print("%s. %s"%(test_case_num,dp[n-1][1]))

