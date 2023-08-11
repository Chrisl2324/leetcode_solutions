class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        lst = list(s)
        left, right = 0, len(lst) - 1
        
        while left < right:  
            while left < right and lst[left] not in vowels:
                left += 1
            while left < right and lst[right] not in vowels:
                right -= 1
    
            if left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
              
        result = ''.join(lst)
        return result

       



        