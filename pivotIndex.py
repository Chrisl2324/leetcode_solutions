class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums) - 1):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i 
            left_sum += nums[i]
        return -1

  

