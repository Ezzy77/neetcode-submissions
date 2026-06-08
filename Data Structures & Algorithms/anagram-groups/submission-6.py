class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            orderd = "".join(sorted(s))
            results[orderd].append(s)
        return list(results.values())
        
        
        