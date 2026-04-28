class FreqStack:

    def __init__(self):
        self.freqstack = {}
        self.stack = []
        

    def push(self, val: int) -> None:
        self.freqstack[val] = self.freqstack.get(val,0)+1
        self.stack.append(val)

        
    def pop(self) -> int:

        max_cnt = max(self.freqstack.values())

        for i in range(len(self.stack)-1,-1,-1):
            num = self.stack[i]
            if self.freqstack[num] == max_cnt:
                self.stack.pop(i)
                self.freqstack[num] -= 1
                return num
