class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        sortedfreq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sortedfreq[:k]]
        