def solution(new_id):

    #1단계
    new_id=new_id.lower()
    print("1단계 :",new_id)

    #2단계
    for i in new_id:
        if i.isalpha() or i == '.' or  i == '_' or i == '-' or i.isdigit():
            continue
        else:
            new_id = new_id.replace(i,"")

    print("2단계 :",new_id)

    #3단계
    while('..' in new_id):
        new_id = new_id.replace('..','.')

    print("3단계 :",new_id)

    #4단계
    if len(new_id)>=2:
        while (new_id[0]=='.' or new_id[-1]=='.'):
            if (new_id[0]=='.'):
                new_id=new_id[1:]
            elif (new_id[-1]=='.'):
                new_id=new_id[:-1]

    print("4단계 :",new_id)

    #5단계
    if new_id=='':
        new_id += 'a'
    
    print("5단계 :",new_id)
    
    #6-7단계
    if len(new_id) >= 16:
        new_id=new_id[:15]
        if (new_id[-1]=='.'):
            new_id=new_id[:-1]
    elif len(new_id) <=2:
        addstr=new_id[-1]
        while (len(new_id)!=3):
            new_id += addstr

    print("막단계 :",new_id)
            
    return new_id

