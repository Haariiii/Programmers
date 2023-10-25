def solution(k, m, score):
    answer = 0
    x = len(score) // m
    score.sort(reverse=True)
    
    for i in range(0, x * m, m):
        answer += min(score[i:i+m]) * m
    return answer