class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        #sorting,if sorted duplicate values would be adjcent to eachother

        # nums.sort()
    
        # l, r = 0, 1
        # while r < len(nums):
        #     if nums[l] == nums[r]:
        #         return True
        #     l+= 1
        #     r+= 1
        # return False

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


        