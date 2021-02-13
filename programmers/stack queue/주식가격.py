def solution(prices):
    answer = []
    for i in range(len(prices)):
        count=0
        for j in range(i+1,len(prices),1):
            if prices[i]<=prices[j]:
                count = count + 1
                print(count)
            else:
                count = count +1 
                break
                    
        answer.append(count)
        print(answer)
                
    return answer

print(solution([1, 2, 3, 2, 3]))
