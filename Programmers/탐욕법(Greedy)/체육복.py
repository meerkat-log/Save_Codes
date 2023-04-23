# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]

    for i in _reserve:
        if i - 1 in _lost:
            _lost.remove(i-1)
        elif i + 1 in _lost:
            _lost.remove(i+1)
    return n - len(_lost)
