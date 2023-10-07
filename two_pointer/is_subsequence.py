class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
        l = 0
        for i in range(len(t)):
            if (l == len(s)):
                return True
            if  t[i] == s[l]:
                l += 1

        return l == len(s)
