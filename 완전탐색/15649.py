import sys
from itertools import permutations
input = sys.stdin.readline
n,m=map(int,input().split())
numlist= [i for i in range(1,n+1)]

for re in permutations(numlist,m):
    for r in re:
        print(r,end=' ')
    print()