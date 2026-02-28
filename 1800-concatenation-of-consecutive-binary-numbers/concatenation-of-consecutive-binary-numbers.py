class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        bitLen = 1
        next_power = 2

        for i in range(1,n+1):
            if i == next_power:
                bitLen += 1
                next_power *= 2
            ans = ((ans << bitLen) + i) % MOD
        return ans
        