class Solution:
    
    def findSetBits(self, num2: int) -> int:
        counter = 0
        while num2 != 0:
            num2 = num2 & (num2 - 1)
            counter += 1
        return counter
    
    def minimizeXor(self, num1: int, num2: int) -> int:
        numSetBits = self.findSetBits(num2)
        result = 0
        
        for i in range(31, -1, -1):
            if (num1 & (1 << i)) != 0 and numSetBits > 0:
                result |= (1 << i)
                numSetBits -= 1
        
        index = 0
        while numSetBits > 0:
            if (result & (1 << index)) == 0:
                result |= (1 << index)
                numSetBits -= 1
            index += 1
        
        return result