def solution(s, n):
    answer = ''
    for i in s:
        if i==" ":
            answer+=" "
        else:
            ascii=ord(i)
            if (i.isupper() and ascii+n>ord('Z')):
                answer+=chr(ord('A')-1+(ascii+n-ord('Z')))
            elif (i.islower() and ascii+n>ord('z')):
                answer+=chr(ord('a')-1+(ascii+n-ord('z')))
            else:
                answer += chr(ascii+n)
    return answer