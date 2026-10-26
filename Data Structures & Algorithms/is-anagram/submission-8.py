class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for a in s:
            s_dict[a] = s_dict.get(a,0)+1
        for aa in t:
            t_dict[aa] = t_dict.get(aa,0)+1
        return s_dict == t_dict
        