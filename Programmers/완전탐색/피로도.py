# https://school.programmers.co.kr/learn/courses/30/lessons/87946

answer = 0


def dfs_dungeons(k, dungeons, count, clear):
    global answer

    for i in range(len(dungeons)):
        if answer < count:
            answer = count

        if clear[i] == 0 and k >= dungeons[i][0]:
            clear[i] = 1
            dfs_dungeons(k - dungeons[i][1], dungeons, count + 1, clear)
            clear[i] = 0


def solution(k, dungeons):
    global answer

    for i in range(len(dungeons)):
        clear = [0] * len(dungeons)
        clear[i] = 1
        count = 1

        dfs_dungeons(k - dungeons[i][1], dungeons, count, clear)

    return answer
