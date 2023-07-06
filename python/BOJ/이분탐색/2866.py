import sys
input = sys.stdin.readline

r, c= map(int, input().split())
table =[]
for _ in range(r):
    table.append(list(input()))

start = 0
end = r-1
while start<=end:
    mid = (start+end)//2
    words = []
    exist = False
    for y in range(c):
        word = ""
        for x in range(mid,r):
            word += table[x][y]
        if word in words:
            exist = True
            break
        else:
            words.append(word)
    if exist:
        end = mid-1
    else:
        start = mid+1
print(start-1)