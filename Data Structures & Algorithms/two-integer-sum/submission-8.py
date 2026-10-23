class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # INT array and INT target number
        # OUTPUT -> int [], that contains two indices such
        #thatnumbers at those indeces sums up to tartget int

        # nums[i] + nums[j] = target <=> nums[j] = target - nums[i]
        amap = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in amap:
                return [amap[comp], i]

            amap[v] = i



        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        
        