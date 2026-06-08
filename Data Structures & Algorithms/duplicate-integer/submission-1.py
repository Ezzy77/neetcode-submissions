class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for n in nums:
            if n not in countMap:
                countMap[n] = 1
            else:
                return True
        return False
        
         