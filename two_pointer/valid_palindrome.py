class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleared = ''.join(ch for ch in s if ch.isalnum()).lower()
        
        return cleared == cleared[::-1]
