class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            freq[n] += 1
        
        for n, cnt in freq.items():
            buckets[cnt].append(n)
        print(buckets)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
     

   



        