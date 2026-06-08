class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force by sorting the string
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        return False        