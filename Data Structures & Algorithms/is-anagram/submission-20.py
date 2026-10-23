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
        countS, countT = defaultdict(int), defaultdict(int)
        for char in s:
            countS[char] += 1
        for char in t:
            countT[char] += 1
        

        return countS == countT

        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        