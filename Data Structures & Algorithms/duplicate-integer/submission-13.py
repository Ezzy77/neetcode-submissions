class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # on2 time and o1 space solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if  nums[i] == nums[j]: return True
        # return False


        # on time and on spCE
        seen  = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False



        