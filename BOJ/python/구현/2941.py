import sys
input = sys.stdin.readline

s = input()
alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
idx = 0
answer = 0

while idx+1 < len(s):
    for length in range(3,0,-1):
        if length == 1:
            answer += 1
            idx += 1
        elif idx+length < len(s) and s[idx:idx+length] in alphabet:
            answer+=1
            idx += length
            break
        
print(answer)