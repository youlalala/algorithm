from itertools import product
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
numlist=[i for i in range(1,n+1)]

for re in product(numlist,repeat=m):
    for r in re:
        print(r,end=' ')
    print()