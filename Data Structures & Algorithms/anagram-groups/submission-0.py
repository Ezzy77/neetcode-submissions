from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hash map

        # defaultdict automatically creates non existing key with default values
        groups = defaultdict(list)

        for word in strs:
            # use sorted string version as key
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

        