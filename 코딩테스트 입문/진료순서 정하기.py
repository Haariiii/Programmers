def solution(emergency):
    answer = []
    sub = sorted(emergency, reverse=True)

    for n in emergency:
        answer.append(sub.index(n) + 1)
    return answer