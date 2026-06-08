class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        countS = defaultdict(int)
        countT = defaultdict(int)

        for i, n in enumerate(s):
            countS[n] += 1
        for i, n in enumerate(t):
            countT[n] += 1
        return countS == countT
        