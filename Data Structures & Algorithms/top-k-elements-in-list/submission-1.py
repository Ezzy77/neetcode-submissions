class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive approach
        freq = defaultdict(int)

        # Step 1: Count frequency
        for n in nums:
            freq[n] += 1

        # Step 2: Sort by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        # Step 3: Take first k elements (only keys)
        result = [item[0] for item in sorted_items[:k]]

        return result


        