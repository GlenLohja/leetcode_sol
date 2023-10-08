class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        occurrence = -1
        for i in range(len(haystack)):
            if haystack[i:len(needle) + i] == needle:
                occurrence = i
                return occurrence
        return occurrence
