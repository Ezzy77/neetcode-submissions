class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-num for num in nums]

        # heapq.heapify(nums)
        # largest = 0

        # for _ in range(k):
        #     largest = -heapq.heappop(nums)
        # return largest
        # time = o(n + klogn)

        return heapq.nlargest(k, nums)[-1]



        
        