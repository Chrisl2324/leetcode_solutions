class Solution(object):
    @staticmethod
    def gcdOfString(word1, word2):
        def gcd(a, b):
            while b:
                a, b = b, a % b 
            return a

        gcd_len = gcd(len(word1), len(word2))
        common_substring = word1[:gcd_len]

        if word1 + word2 == word2 + word1 and common_substring * (len(word1) // gcd_len) == word1 and common_substring * (len(word2) // gcd_len) == word2:
            return common_substring
        else:
            return ""



