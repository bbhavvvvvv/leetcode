class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = 0
        b = 0
        for x in s:
            if x == 'b':
                b+=1
            else:
                if b>0:
                    a+= 1
                    b -= 1
        return a