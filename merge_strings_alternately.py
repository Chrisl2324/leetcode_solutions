class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ''
        i = 0
        max_length = len(max(word1, word2))
        while i < max_length:
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
            
        result += word1[i:]
        result += word2[i:]
        return result
        

       
