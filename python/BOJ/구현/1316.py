import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

result = 0
for _ in range(n):
    cnt = dict()
    word = deque(list(input().strip()))
    before =""
    for w in word:
        # 연속해서 나타남
        if w == before:
            continue
        # 떨어져서 나타남
        if w in cnt.keys():
            cnt[w] = 0
        else:
            cnt[w] = 1
        before = w
    if 0 not in cnt.values():
        result += 1
print(result)


