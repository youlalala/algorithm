import sys
input = sys.stdin.readline
 
# 홍준이가 적은 자연수 n개
n = int(input())

num_list = list(map(int,input().split()))

# 홍준이가 명우에게 질문한 수 m 개
m = int(input())

# 시작 n ~ 끝 n
answer = [[False]* n for _ in range(n)]
def palindrome():
    global answer

    # s~e 길이가 1인 경우
    for i in range(n):
        answer[i][i] = True
    
    # s~e 길이가 2인 경우
    for i in range(n-1):
        if num_list[i] == num_list[i+1]:
            answer[i][i+1] = True

    # s~e 길이가 3이상인 경우
    for length in range(2,n):
        for start in range(n-length):
            end = start + length
            if num_list[start] == num_list[end] and answer[start+1][end-1]:
                answer[start][end] = True

palindrome()
for _ in range(m):
    s, e = map(int, input().split())
    # 팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력한다.
    if answer[s-1][e-1]:
        print("1")
    else:
        print("0")
    
