class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute solution envolves counting frequency
        # store k, v pairs in array then sort the array based on freq
        # then get top K

        # count = defaultdict(int)
        # for n in nums:
        #     count[n] += 1
        
        # arr = []
        # for n, cnt in count.items():
        #     arr.append([cnt, n])
        
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
       
        # return res

        # more efficient solution uses bucket sort
        count = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n, cnt in count.items():
            bucket[cnt].append(n)

        res = []
        
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
       
        return res
            


        