import sys
input = sys.stdin.readline

# 행성 간 플로우 개수
n = int(input())
# 플로우 관리 비용
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


# 모든 행성을 연결하면서 플로우 관리 비용 최소화하기
def find_parent(parent, x):  
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b): 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n)]
def kruskal():
    edges = [] 
    for i in range(1, n):
        for j in range(i):
            edges.append((graph[i][j], i, j))
    edges.sort()

    answer = 0
    for cost, a, b in edges: 
        if find_parent(parent, a) != find_parent(parent, b): 
            union(parent, a, b)
            answer += cost
    return answer

print(kruskal())