class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False

        countS = defaultdict(int)
        countT = defaultdict(int)

        for ch in s:
            countS[ch] += 1
        for ch in t:
            countT[ch] += 1
        return countS == countT
        