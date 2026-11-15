class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # first convert to negative value to use python min heap
        stones = [-stone for stone in stones]

        heapq.heapify(stones)
        print(stones)
        
        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(x -y))
        return -stones[0] if stones else 0

        