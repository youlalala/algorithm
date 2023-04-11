import sys

input = sys.stdin.readline

n, k = map(int, input().split())
min_weight = 500
kit_list = list(map(int, input().split()))

visited = [False] * n
kit_order = []
result = 0
weight = min_weight


def dfs(order, w):
    global result

    if len(order) == n:
        result += 1
        return

    # n일동안의 경우의수
    for i in range(n):
        if not visited[i] and w - k + kit_list[i] >= min_weight:
            w = w - k + kit_list[i]
            order.append(kit_list[i])
            visited[i] = True
            dfs(order, w)
            visited[i] = False
            order.remove(kit_list[i])
            w = w + k - kit_list[i]


dfs(kit_order, weight)
print(result)
