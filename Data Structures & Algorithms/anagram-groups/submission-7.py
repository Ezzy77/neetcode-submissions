class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table  = defaultdict(list)

        for s in strs:
            sorteds = "".join(sorted(s))
            table[sorteds].append(s)
        return list(table.values())


        