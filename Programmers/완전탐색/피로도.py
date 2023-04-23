# https://school.programmers.co.kr/learn/courses/30/lessons/87946

answer = 0

# 깊이 우선 탐색 방법을 사용하기 위한 DFS 함수 생성
# DFS는 재귀함수로 구현되어 방문했던 노드를 반드시 알고 있어야 한다.
# count는 어느 정도의 깊이까지 들어왔는지  확인하기 위한 변수이다. 호출될 때마다 1씩 증가된다.
# 따라서 dungeons 배열과 같은 길이를 가지는 clear라는 배열을 전달한다.
# clear 배열은 방문했던 던전을 확인하기 위한 배열로 방문했다면 1로 하지 않았다면 0으로 표시한다.
def dfs_dungeons(k, dungeons, count, clear):
    global answer

#   모든 길을 다 탐색해야 하기 때문에 dungeons 배열의 길이 그대로 반복한다.
    for i in range(len(dungeons)):

#       점점 깊이 들어갈수록 count의 값이 증가되기 때문에 전역변수로 생성한 answer 변수보다 count의 값이 크다면
#       최대로 탐험할 수 있는 던전의 수가 늘어난 것이기 때문에 answer의 값을 count 값으로 변경한다.
        if answer < count:
            answer = count

#       방문하지 않았던 던전이면서 현재 피로도가 던전을 탐험할 때 필요한 최소 필요 피로도보다 크거나 같다면 던전을 탐험한다.
#       최소 필요 피로도는 소모 필요도보다 항상 크거나 같기 때문에 모든 노드를 탐색하는 DFS 방식으로는 소모 피로도를 생각하지 않아도 된다.
        if clear[i] == 0 and k >= dungeons[i][0]:

#           i번째 던전을 새롭게 탐험할 수 있기 때문에 clear 배열에서 i번째 던전을 방문한 던전으로 업데이트한다.
            clear[i] = 1
            
#           새로운 던전을 탐험하게 되었기 때문에 현재 피로도와, 탐험한 던전의 개수, 탐험한 던전의 배열을 가지고 재귀호출을 하게 된다. 
            dfs_dungeons(k - dungeons[i][1], dungeons, count + 1, clear)

#           재귀함수가 끝나면 다른 순서로 탐색하기 위해 방문했던 던전을 방문하지 않은 것으로 초기화한다.
            clear[i] = 0


def solution(k, dungeons):
    global answer
    clear = [0] * len(dungeons)
    count = 1
    
    for i in range(len(dungeons)):
        clear[i] = 1
        dfs_dungeons(k - dungeons[i][1], dungeons, count, clear)
        clear[i] = 0

    return answer
