class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val = n & 1
        
        while n != 0:
            n >>= 1
            if val == (n & 1):
                return False
            val = n & 1
        return True
        