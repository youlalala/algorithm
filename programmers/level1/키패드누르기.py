def solution(numbers, hand):
    result=""
    phone=dict([(1,1),(2,1),(3,1),(4,2),(5,2),(6,2),(7,3),(8,3),(9,3),('*',4),(0,4),('#',4)])
    leftHand='*'
    rightHand='#'
    for i in numbers:
        print("왼손:", leftHand)
        print("오른손:",rightHand)
        if i==1 or i==4 or i==7:
            result+="L"
            leftHand=i
        elif i==3 or i==6 or i==9:
            result+="R"
            rightHand=i
        else:
            if (rightHand==2 or rightHand==5 or rightHand==8 or rightHand==0) and (leftHand==2 or leftHand==5 or leftHand==8 or leftHand==0):
                r_dist=abs(phone[i]-phone[rightHand])
                l_dist=abs(phone[i]-phone[leftHand])      
            elif leftHand==2 or leftHand==5 or leftHand==8 or leftHand==0:
                r_dist=abs(phone[i]-phone[rightHand])+1
                l_dist=abs(phone[i]-phone[leftHand])
            elif (rightHand==2 or rightHand==5 or rightHand==8 or rightHand==0):
                r_dist=abs(phone[i]-phone[rightHand])
                l_dist=abs(phone[i]-phone[leftHand])+1
            else:
                l_dist=abs(phone[i]-phone[leftHand])+1
                r_dist=abs(phone[i]-phone[rightHand])+1
            print("left거리",l_dist)
            print("right거리",r_dist)
            if l_dist<r_dist:
                result+="L"
                leftHand=i
            elif l_dist>r_dist:
                result+="R"
                rightHand=i
            else:
                if hand=="right":
                    result+="R"
                    rightHand=i
                else:
                    result+="L"
                    leftHand=i
        print(result)


    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))