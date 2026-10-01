class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        arr = []
        for key, cnt in count.items():
            arr.append([key, cnt])
        
        arr.sort(key=lambda x:x[1])
        res = []
        for i in range(len(arr)-1, -1, -1):
            res.append(arr[i][0])

            if len(res) == k:
                break

        
        return res


        