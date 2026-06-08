class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)

        # for n in nums:
        #     freq[n] += 1
        # sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        # return [item[0] for item in sorted_items[:k]]

        # using bucket sort
        freq = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freq[n] += 1
        
        for num, count in freq.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
