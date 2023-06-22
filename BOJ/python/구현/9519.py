import sys
input = sys.stdin.readline

n=int(input())
words = list(input().strip())

cnt = len(words)//2
front = words[:cnt+1]
rear = words[cnt+1:]
rotate=[words]

while True:
    front = words[:cnt+1]
    rear = words[cnt+1:]
    newwords = []
    for i in range(len(rear)):
        newwords.append(front.pop(0))
        newwords.append(rear.pop())
    newwords += front

    if rotate[0] == newwords:
        break
    rotate.append(newwords)
    words = newwords.copy()

rotate = [rotate[0]] + rotate[1:][::-1]
print(''.join(rotate[n%len(rotate)]))
