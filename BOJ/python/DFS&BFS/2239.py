import sys
input = sys.stdin.readline

def row_isExist(x,y,num):
    if num in nums[x]:
        return True
    else:
        return False

def col_isExist(x,y,num):
    for i in range(9):
        if num == nums[i][y]:
            return True
    return False

def square_isExist(x,y,num):
    row = x//3
    col = y//3
    for i in range(row*3,row*3+3):
        for j in range(col*3,col*3+3):
            if num == nums[i][j]:
                return True
    return False

def dfs(zero_idx):
    if zero_idx == len(zero_list):
        for nn in nums:
            print(''.join(map(str,nn)))
        exit()
        return
    a,b = zero_list[zero_idx]
    for n in range(1,10):
        if not row_isExist(a,b,n) and not col_isExist(a,b,n) and not square_isExist(a,b,n):
            nums[a][b] = n
            dfs(zero_idx+1)
            nums[a][b] = 0

nums = []
zero_list=[]
for i in range(9):
    nums.append(list(map(int,input().strip())))
    for j in range(9):
        # 0인 곳 좌표 찾기
        if nums[i][j] == 0:
            zero_list.append((i,j))

dfs(0)
