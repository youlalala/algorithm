import sys
input = sys.stdin.readline

# 기타 수
n = int(input())

# 시리얼 번호
serials = []
for _ in range(n):
    serial_num = input().strip()
    # 숫자들의 합
    num_sum = 0
    for serial in serial_num:
        if serial.isdigit():
            num_sum += int(serial)
    serials.append((serial_num, len(serial_num), num_sum))


# A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
serials.sort(key=lambda x:(x[1], x[2], x[0]))

for s in serials:
    print(s[0])
