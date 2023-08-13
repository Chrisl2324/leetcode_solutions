class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]
        return answer


