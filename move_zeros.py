class Solution(object):
    def moveZeros(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == 0 and nums[right] != 0:
                nums.append(nums.pop(left))
            left += 1
            right -= 1
        return nums
    
    
if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    result = sol.moveZeros(nums)
    print(result)