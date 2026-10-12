class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for c in s.lower():
            if not c.isalnum():
                continue
            news += "".join(c.split())
        return news == news[::-1]

            
            


        