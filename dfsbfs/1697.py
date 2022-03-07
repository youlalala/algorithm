import sys
from collections import deque
input=sys.stdin.readline

n,k = map(int,input().split())
map=[0]*100001
queue=deque([n])
while queue:
    n=queue.popleft()
    if (n == k):
        break
    nums=[n+1,n-1,2*n]
    for num in nums:
        if 0 <= num <= 100000 and map[num]==0:
            map[num]=map[n]+1
            queue.append(num)
print(map[k])