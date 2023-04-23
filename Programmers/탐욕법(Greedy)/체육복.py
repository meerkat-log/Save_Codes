# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    
#   배열이 정렬되어 있다고 하지 않았기 때문에 -1, +1한 결과값을 쉽게 사용하기 위해 정렬
    lost.sort()
    reserve.sort()

#   여벌의 체육복을 가져왔지만 도난당한 경우 못 빌려주므로 해당 경우를 제외한 새로운 배열 생성
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]

    for i in _reserve:
#       여벌의 체육복을 가진 i번째 학생이 i-1번 학생에게 빌려줄 수 있는 경우
        if i - 1 in _lost:
            _lost.remove(i-1)

#       여벌의 체육복을 가진 i번째 학생이 i+1번 학생에게 빌려줄 수 있는 경우
        elif i + 1 in _lost:
            _lost.remove(i+1)
    
    return n - len(_lost)
