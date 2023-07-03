import sys
import math

input = sys.stdin.readline
a,b = map(int,input().split())
c,d = map(int,input().split())

y = b * d
x = a*d + b*c

z = math.gcd(x,y)
print(x//z,y//z)