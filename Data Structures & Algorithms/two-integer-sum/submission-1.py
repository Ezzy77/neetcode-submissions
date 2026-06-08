class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in hashM:
                return [hashM[comp], i]
            hashM[n] = i
        
        