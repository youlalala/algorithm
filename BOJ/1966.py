from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    # n : 문서의 개수, m : 몇번째로 인쇄되었는 지 궁금한 문서가 현재 큐에서 몇번째인지
    n, m = map(int, input().split())
    # 문서의 중요도
    important = list(map(int, input().split()))
    # 문서 index 넣어주기
    q = deque([])
    for i in range(n):
        q.append((important[i],i))

    copy_completed = 0
    while q:
        first, idx = q.popleft()
        success = True
        for element, _ in q:
            if element > first:
                q.append((first,idx))
                success = False
                break
        if success:
            copy_completed += 1
            if idx == m:
                break
    print(copy_completed)