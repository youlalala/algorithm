# n : 사람 수, m : 파티 수
people_num, party_num = map(int, input().split())
# 진실을 아는 사람의 수와 번호

truth = input()
truth_num = int(truth[0])
truth_list = []
if truth_num != 0:
    truth_list = list(map(int,truth[1:].split()))
    
# 각 파티마다 오는 사람의 수와 번호
parties = []
for _ in range(party_num):
    parties.append(list(map(int,input().split()))[1:])

party_success = [True] * len(parties)

def find_truth_people(n):
    for i in range(len(parties)):
        if n in parties[i]:
            party_success[i] = False
        # 그 파티에 참석한 사람은 모두 진실을 아는 사람
        if not party_success[i]:
            for p in parties[i]:
                if p not in find_list:
                    find_list.append(p)
                    find_truth_people(p)
                    

# 진실을 아는 사람 모두 찾기
find_list = []
for truth in truth_list:
    find_list.append(truth)      
    find_truth_people(truth) 

answer = party_success.count(True)
print(answer)
