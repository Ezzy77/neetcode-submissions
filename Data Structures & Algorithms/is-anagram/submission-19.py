class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # INPUT -> string t and string s
        # OUTPUT -> True or False

        # Compare char frequenecy

        # 1) Compare the lenght, as diff length can not be anagram
        # 2) sort both string
        # 3) compare if they are same string

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        