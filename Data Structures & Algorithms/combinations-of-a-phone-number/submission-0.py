class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        wordlist = []
        hashmap = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"],
                    "6":["m","n","o"],"7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        for digit in digits:
            wordlist.append(hashmap[digit])
            # print(wordlist)

        def dfs(i, curr):
            if i == len(wordlist):
                res.append(curr)
                return 
            for char in wordlist[i]:
                dfs(i+1,curr+char)
        if digits:
            dfs(0,"")
        return res