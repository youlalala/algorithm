import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    cmds = input().strip()
    print(cmds)
    print(s)
    if cmds == "all":
        s = set()
        for i in range(1,21):
            s.add(i)
        continue
    elif cmds == "empty":
        s= set()
        continue
    cmd, num = cmds.split()
    num = int(num)
    if cmd == "add":
        s.add(num)
    elif cmd == "remove":
        if num in s:
            s.remove(num)
    elif cmd == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    
