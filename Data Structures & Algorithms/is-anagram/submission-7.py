class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return sorted(s) == sorted(t)
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        # walk through t and reduce the count
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            # if we used ch more times in t than it appeared in s
            if count[ch] < 0:
                return False
        # 4) At this point, because len(s) == len(t) and no count went negative,
        # all counts must be zero — we can return True directly
        return True


        # One Time Pass
        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT
        