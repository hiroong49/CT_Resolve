# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    y, m, d = map(int, today.split('.'))
    tod = y * 12 * 28 + m * 28 + d   # 연일월 각각 하나씩 비교하는 것보다 계산/코드가 간결
    
    # 약관종류와 유효기간 딕셔너리에 저장
    for i in terms:
        typ, exp = i.split()
        dic[typ] = int(exp)
        
    for i, s in enumerate(privacies):
        date, t = s.split()
        year, month, day = map(int, date.split('.'))
        month += dic[t]     # 약관에 따른 유효기간 계산
        priv = year * 12 * 28 + month * 28 + day

        # 유효기간이 지난 것 answer 배열에 저장 (정보는 이전 날짜까지만 저장할 수 있음)        
        if priv <= tod:
            answer.append(i+1)
            
    return answer