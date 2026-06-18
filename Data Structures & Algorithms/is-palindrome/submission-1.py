class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        if s==s[::-1]:
            return True
        return False    