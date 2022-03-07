import math
import  sys
input = sys.stdin.readline

def isPrime(n):
    if(n==1):
        return False
    if(n>2):
        # 2~n의 제곱근까지 모든 수 확인
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                #소수가 아님
                return False
    # 소수임
    return True

m,n = map(int,input().split())
for i in range(m,n+1):
    if isPrime(i):
        print(i)



##에라토스테네체 (다른방법)
# array=[True for i in range(n+1)]
# print(array)
# for i in range(2,int(math.sqrt(n))+1):
#     if array[i]==True:
#         j=2
#         while i*j<=n:
#             array[i*j]=False
#             j+=1
# for i in range(m,n+1):
#     if array[i]:
#         print(i)




