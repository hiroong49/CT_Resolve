# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
            
        if numbers[i] % 3 == 1:
            left = numbers[i]
            answer += 'L'
        elif numbers[i] % 3 == 0:
            right = numbers[i]
            answer += 'R'
        else:
            # 위로 올라 가면 -3, 아래로 내려 가면 +3
            # 왼쪽은 -1, 오른쪽은 +1
            mL = abs(numbers[i] - left)
            mR = abs(numbers[i] - right)
            dL = (mL // 3) + (mL % 3)
            dR = (mR // 3) + (mR % 3)

            if dL > dR:
                right = numbers[i]
                answer += 'R'
            elif dL < dR:
                left = numbers[i]
                answer += 'L'
            else:
                if hand == 'left':
                    left = numbers[i]
                    answer += 'L'
                else:
                    right = numbers[i]
                    answer += 'R'
                    
    return answer