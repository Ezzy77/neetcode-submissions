class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = {}

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in myset:
                return [myset[compl],i]
            myset[nums[i]] = i



        