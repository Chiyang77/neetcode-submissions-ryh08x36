class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if not word:
            return 0
        alpha = {}
        for i,k in enumerate(keyboard):
            alpha[k]=i

        cnt = 0
        cnt += alpha[word[0]]
        prev = alpha[word[0]]
        for s in word[1:]:
            move = abs(prev-alpha[s])
            cnt+=move
            prev = alpha[s]
        return cnt





        