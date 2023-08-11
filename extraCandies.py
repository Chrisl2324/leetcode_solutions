class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = [(candy + extraCandies) >= max(candies) for candy in candies]
        return result 
    
    

