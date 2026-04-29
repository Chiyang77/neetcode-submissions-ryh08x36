class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return 
        if len(strs)==1:
            return strs[0]


        minlen = float('inf')
        for str in strs:
            minlen = min(minlen, len(str))

        i = 0
        while i < minlen:
            first = strs[0][i]
            for str in strs:
                if str[i] == first:
                    continue
                else:
                    return strs[0][:i]

            i +=1
        return strs[0][:i]