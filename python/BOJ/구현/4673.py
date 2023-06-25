def cal(n):
    sum=n
    for i in str(n):
        sum+=int(i)
    return sum

numlist=[]
for i in range(1,10001):
    num=cal(i)
    if(num<=10000):
        numlist.append(num)

for i in range(1,10001):
    if(i not in numlist):
        print(i)