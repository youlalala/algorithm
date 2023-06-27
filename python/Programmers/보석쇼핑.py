def solution(gems):
    answer = []
    # 모든 보석의 종류
    type_cnt = len(set(gems))
    min_term = len(gems)

    # 투포인터
    start = 0
    end = 0
    buy_type_cnt = dict()
    buy_type_cnt[gems[start]] = 1

    while start<= end:
        if len(buy_type_cnt) == type_cnt:
            if min_term > end-start:
                min_term = end-start
                answer = [start+1, end+1]
            else:
                if buy_type_cnt[gems[start]] == 1:
                    del buy_type_cnt[gems[start]]
                else:
                    buy_type_cnt[gems[start]] -= 1
                start += 1
        elif len(buy_type_cnt) < type_cnt:
            end += 1
            if end == len(gems):
                break
            if gems[end] not in buy_type_cnt:
                buy_type_cnt[gems[end]] = 1
            else:
                buy_type_cnt[gems[end]] += 1
    return answer