def solution(a, b):
    day=0
    if a>1:
        for month in range(1,a):
            if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                day += 31
                continue
            elif month==2:
                day += 29
                continue
            elif month==4 or month==6 or month==9 or month==11:
                day += 30
                continue
        day += b
    elif a==1:
        day += b
    day -= 1
    kk=day%7
    daylist=['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    answer = daylist[kk]
    
    return answer