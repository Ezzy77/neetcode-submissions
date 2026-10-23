class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # INT array and INT target number
        # OUTPUT -> int [], that contains two indices such
        #thatnumbers at those indeces sums up to tartget int

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        