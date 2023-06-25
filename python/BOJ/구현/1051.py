import sys
input=sys.stdin.readline

size = 1
n,m = map(int,input().split())
numlist = [list(input()) for _ in range(n)]
for i in range(n-1):
    for j in range(m-1):
        num = numlist[i][j]
        for k in range(i+1,n):
            if numlist[k][j] == num:
                length = k-i
                if (i+length<n) and (j+length<m):
                    if (numlist[i][j+length] == num) and (numlist[i+length][j+length]==num):
                        size = max(size,length+1)
                
print(size**2)
