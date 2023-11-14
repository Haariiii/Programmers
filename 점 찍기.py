def solution(k, d):
    answer = 0
    a, b = 0, 0
    n_list = []
    while (pow(a*k, 2) + pow(b*k, 2)) ** 0.5 <= d:
        answer += 1
        n_list.append(b*k)
        b += 1
    for a in n_list[1:]:
        for b in n_list:
            if (pow(a*k, 2) + pow(b*k, 2)) > (d ** 2):
                break
            else: answer += 1
    return answer




res = solution(2, 4)
print(res)