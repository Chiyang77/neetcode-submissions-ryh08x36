class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mapping = {}
        ss = s.split(" ")
        unique = set()
        if len(ss)!= len(pattern):
            return False

        for p,sss in zip(pattern, ss):

            if p not in mapping:
                
                if sss not in unique:
                    mapping[p]=sss
                    unique.add(sss)
                else:
                    return False

                continue
            else:
                if mapping[p]!=sss:
                    return False

        return True


        