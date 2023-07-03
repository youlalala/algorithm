import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
INF = int(1e9)

if n==1:
    print(0)
    sys.exit()
    
visited = [0]*n
q = deque([0])
while q:
    now = q.popleft()
    possible = numbers[now]
    if now+possible >= n-1:
        print(visited[now]+1)
        sys.exit()
    else:
        end = now+possible
    for i in range(now+1,end+1):
        if not visited[i]:
            visited[i] = visited[now]+1
            q.append(i)
    print(visited)

print(-1)
