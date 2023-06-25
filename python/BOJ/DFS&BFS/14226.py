from collections import deque
import sys
input = sys.stdin.readline

s = int(input())
# 이모티콘 수 , 클립보드 수
visited = [[False]*1001 for _ in range(1001)]
q = deque([[1,0,0]])
visited[1][0] = True
if s == 1:
    print(0)
    exit()
while q:
    emoticon, clipboard,time = q.popleft()
    if emoticon == s:
        print(time)
        break
    for n in range(1,4):
        if n==1:
            # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
            n_emoticon, n_clipboard = emoticon, emoticon
        elif n==2:
            # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
            if clipboard == 0:
                continue
            n_emoticon, n_clipboard = emoticon+clipboard, clipboard
        elif n==3:
            # 화면에 있는 이모티콘 중 하나를 삭제한다.
            n_emoticon, n_clipboard = emoticon-1, clipboard
        
        if n_emoticon >= 1001 or n_emoticon<0 or n_clipboard>=1001 or n_clipboard<0 or visited[n_emoticon][n_clipboard]:
            continue

        visited[n_emoticon][n_clipboard]=True
        q.append([n_emoticon,n_clipboard,time+1])
            