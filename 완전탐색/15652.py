from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
numlist=[i for i in range(1,n+1)]

for re in combinations_with_replacement(numlist,m):
    for r in re:
        print(r,end=' ')
    print()