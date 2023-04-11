import sys

input = sys.stdin.readline

def solution(after_num):
    num = 1
    pointer = 0
    while True:
        for n in str(num):
            if n == str(after_num[pointer]):
                pointer += 1
            if pointer == len(after_num):
                return num
        num += 1

print(solution(list(map(int, input().rstrip()))))

