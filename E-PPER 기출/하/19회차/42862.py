# 체육복: 그리디
def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    return n - len(_lost)
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))