from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = defaultdict(list)
        for s in strs:
            ss = tuple(sorted(s))
            hash_dict[ss].append(s)

        return list(hash_dict.values())