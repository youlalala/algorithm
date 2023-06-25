import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [ i for i in range(n+1) ]

def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union(parent,a,b)
    elif check == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")