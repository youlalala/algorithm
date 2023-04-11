import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
B_element = [ list(map(int, input().split())) for _ in range(h+x)]

for i in range(x,h):
    for j in range(y,w):
        B_element[i][j] -= B_element[i-x][j-y]

for k in range(h):
    for element in B_element[k][:w]:
        print(element,end=' ')
    print()