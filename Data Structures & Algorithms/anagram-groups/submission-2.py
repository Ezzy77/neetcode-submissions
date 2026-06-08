class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = defaultdict(list)

        # for s in strs:
        #     sortedString = ''.join(sorted(s))
        #     mymap[sortedString].append(s)
        # return list(mymap.values())

        # o(m * nlogn) time due to sorting, and space of o(m*n)

        # faster solution instead of sorting is to use array inddex of alphabet

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            mymap[tuple(count)].append(s)
        return list(mymap.values())


        