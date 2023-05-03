# https://leetcode.com/problems/jump-game/description/

class Solution:
    def canJump(self, nums: List[int]) -> bool: 
      len_nums = len(nums) # 배열의 길이 저장
      tmp = nums[0] # 배열의 가장 첫번째 값 저장
      if len_nums == 1: # 만약 배열의 길이가 1이라면 이미 끝에 도달한 것이기 때문에 True 반환
        return True
      
      for i in range(len_nums): # 인덱스 0부터 배열의 길이 -1까지 반복
        if tmp == 0: # 반복문이 끝나지 않았는데 점프 할 수 있는 거리가 0이라면 이동 불가하므로 False 반환
          return False

        tmp -= 1 # 한칸씩 점프할 때마다 tmp에 저장된 점프할 수 있는 최대거리가 줄어듦

        if nums[i] > tmp: # 이동한 곳의 값이 현재 점프할 수 있는 거리보다 크다면 해당 값으로 새로 점프 시작
            tmp = nums[i]

        if i + tmp >= len_nums-1: # 현재 위치와 남은 점프 길이가 배열의 끝 인덱스와 같거나 크다면 끝까지 이동할 수 있는 것이므로 True 반환
            return True
