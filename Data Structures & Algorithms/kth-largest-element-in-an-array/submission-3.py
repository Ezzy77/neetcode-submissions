class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-num for num in nums]

        # heapq.heapify(nums)
        # largest = 0

        # for _ in range(k):
        #     largest = -heapq.heappop(nums)
        # return largest
        # time = o(n + klogn)

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) >k:
                heapq.heappop(heap)
        return heap[0]



        
        