class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = nums[i] + nums[j]

        # input : int array, and int target
        # output: array of two indices that adds up to target
        # core challenge: to find the two pairs that adds up to target

        # brute force solution is using nested loop to compare all possibility
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         comp = nums[i] + nums[j]
        #         if comp == target:
        #             return [i, j]
        
        # the time comp is o(n^2)

        # however we coould improve by using a map for o(n) lookup
        prevMap = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in prevMap:
                return [prevMap[comp], i]
            prevMap[n] = i


            

        