class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        n=len(s)
        for i in range(0,n//2):
            if s[i]==s[n-1-i]:
                continue
            else: 
                return False 
        return True          
