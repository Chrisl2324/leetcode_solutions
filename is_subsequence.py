class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        i = 0
        for j in t:
            if s[i] == j:
                i += 1
            if i == len(s):
                return True 
        return False
    


            
            
            

    