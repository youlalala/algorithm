import heapq
n = int(input())
top_list = list(map(int, input().split()))

answer = [0] * len(top_list)
queue = [(top_list[-1],len(top_list)-1)]
for i in range(len(top_list)-2,-1,-1):
    while queue and queue[0][0] < top_list[i]:
        element,idx = heapq.heappop(queue)
        answer[idx] = i+1
    heapq.heappush(queue,(top_list[i],i))
print(" ".join(map(str,answer)))