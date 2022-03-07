import sys

input = sys.stdin.readline
n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())
print(words)

dic=dict()
for word in words:
    print("word",word)
    length=len(word)
    for idx,ele in enumerate(word):
        if(ele in dic):
            dic[ele] += pow(10,length-idx-1)
        else:
            dic[ele] = pow(10,length-idx-1)
print(dic)

dic=sorted(dic.items(),key=lambda x:x[1], reverse=True)
print(dic)

num=9
result=0
for d in dic:
    result += num*d[1]
    num -=1
print(result)
