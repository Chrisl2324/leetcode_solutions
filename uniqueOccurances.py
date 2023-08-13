from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, nums):
        answer = Counter(arr)
        unique = set()
        for value in answer.values():
            if value in unique:
                return False
            unique.add(value)
        return True


