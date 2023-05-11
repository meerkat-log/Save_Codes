# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        answer = []

        while len(answer) < (len(matrix) * len(matrix[0])):
            for i in range(left, right+1): # 왼쪽에서 오른쪽으 이동
                answer.append(matrix[top][i])
            top += 1  # 첫번째 줄이 끝나면 더이상 추가할 값이 없어지므로 +1 하여 하나 행 아래로 이동

            for i in range(top, bottom+1):  # 위에서 아래로 이동 
                answer.append(matrix[i][right])
            right -= 1  # 오른쪽 열을 다 추가하면 해당 열에서 추가할 값이 없어지므로 -1 하여 하나 열 옆으로 이동

            if top <= bottom:
                for i in range(right, left-1, -1):  # 오른쪽에서 왼쪽으로 이동
                    answer.append(matrix[bottom][i])
                bottom -= 1  # 아래 행에서 값이 다 추가되면 더이상 추가할 값이 없어지므로 +1 하여 행을 위로 이동

            if left <= right:
                for i in range(bottom, top-1, -1):  # 아래에서 위로 이동
                    answer.append(matrix[i][left])
                left += 1  # 왼쪽열의 값을 추가하여 더이상 추가할 값이 없어지면 왼쪽 열에서 +1 하여 오른쪽 열로 이동

        return answer
