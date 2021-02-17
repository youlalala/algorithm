def solution(board, moves):
    stk=[]
    cnt=0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] == 0:
                continue
            else:
                stk.append(board[i][move-1])
                board[i][move-1]=0
                break

        if len(stk)>=2:
            if stk[-1]==stk[-2]:
                stk.pop()
                stk.pop()
                cnt+=2
        
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))