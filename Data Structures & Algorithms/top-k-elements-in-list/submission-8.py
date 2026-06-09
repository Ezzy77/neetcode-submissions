class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute solution envolves counting frequency
        # store k, v pairs in array then sort the array based on freq
        # then get top K

        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        arr = []
        for n, cnt in count.items():
            arr.append([cnt, n])
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
       
        return res
            


        