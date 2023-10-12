def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if not set(str(i)) - {'0', '5'}:
            answer.append(i)
    return [-1] if not len(answer) else answer