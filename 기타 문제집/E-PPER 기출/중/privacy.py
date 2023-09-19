# 개인정보 수집 유효기간: 문자열
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire

"""
def solution(today, terms, privacies):
    answer = []
    yy, mm, dd = map(int, today.split('.'))
    terms_dic = {}
    for t in terms:
        k, v = t.split()
        terms_dic[k] = int(v)
    cnt = 1
    for p in privacies:
        date, term = p.split()
        ty, tm, td = map(int, date.split('.'))
        nm = tm + terms_dic[term]
        if nm % 12 == 0:
            ty += nm // 12 - 1
            tm = 12
        else:
            ty += nm // 12
            tm = nm % 12
        print(ty, tm, td)
        if yy > ty or (yy == ty and mm > tm) or (yy == ty and mm == tm and dd >= td):
            answer.append(cnt)
        cnt += 1
    return answer
"""