import sys
input=sys.stdin.readline
# - 기준으로 나누기
n = input().split('-')
print(n)
sum = 0
#
for i in n[0].split('+'):
    sum += int(i)
for i in n[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)