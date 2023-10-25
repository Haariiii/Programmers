def solution(X, Y):
    answer = ''
    # setX, setY = set(X), set(Y)
    # set_ans = set(list(str(X))) & set(list(str(Y)))
    set_ans = set(str(X)) & set(str(Y))
    dic_ans = {}

    if set_ans == set():
        return '-1'
    elif set_ans == set(['0']):
        return '0'
    else:
        for i in set_ans:
            i = str(i)
            temp = str(X).count(i) if str(X).count(i) < str(Y).count(i) else str(Y).count(i)
            dic_ans[int(i)] = temp

        dic_ans = dict(sorted(dic_ans.items(), reverse=True))
        for k, v in dic_ans.items():
            answer += str(k) * v
        return answer