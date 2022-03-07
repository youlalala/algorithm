import sys
input = sys.stdin.readline

x,y=map(int,input().split())
day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
maxDay=[31,28,31,30,31,30,31,31,30,31,30,31]

sum=0
for i in range(0,x-1):
    sum += maxDay[i]
sum+=y

print(day[sum%7])
