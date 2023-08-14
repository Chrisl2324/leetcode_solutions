class Solution(object):
    def isValid(self, s):
        start = '({['
        end = ')}]'
        start_end = {')':'(', '}':'{', ']':'['}
        
        start_tags = []
        for char in s:
            if char in start:
                start_tags.append(char)
            elif char in end:
                if len(start_tags) == 0 or start_end[char] != start_tags.pop():
                    return False 
        return len(start_tags) == 0
    
