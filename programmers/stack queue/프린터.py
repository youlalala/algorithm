def solution(priorities, location):
    answer = 0
    length=len(priorities)
    p1=[]
    p2=[]
    doc=[]
    asc=65

    for i in range(length):
        doc.append(chr(asc))
        asc+=1
    
    an=doc[location]

    while(True):

        for i in range(1,len(doc)):
            if priorities[0]<priorities[i]:
                doc.append(doc.pop(0))
                priorities.append(priorities.pop(0))
                print("대기목록",doc)
                break
            if i==(len(doc)-1):
                p1.append(doc.pop(0))
                p2.append(priorities.pop(0))
                print("대기목록",doc)
                print("print순서",p1)
        if(len(doc)==1):
            p1.append(doc.pop(0))
            p2.append(priorities.pop(0))
            print("대기목록",doc)
            print("print순서",p1)
            

        if(len(p1)==length):
            break
    answer= (p1.index(an))+1
            


    return answer


print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
