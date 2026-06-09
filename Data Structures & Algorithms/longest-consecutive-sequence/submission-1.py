class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        res = 0
        store = set(nums)

        for n in nums:
            streak, current = 0, n
            while current in store:
                streak+=1
                current += 1
            res = max(res, streak)
        return res
        