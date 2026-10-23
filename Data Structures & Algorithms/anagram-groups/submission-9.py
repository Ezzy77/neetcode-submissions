class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {"sorted(s)": ["unsorted s", "hhxs"]}
        count = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            count[sorted_s].append(s)
        output = count.values()
        return list(output)

        