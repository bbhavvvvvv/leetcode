class Solution:
    def minOperations(self, s: str) -> int:
        mismatchA = 0
        mismatchB = 0

        for i, ch in enumerate(s):
            expA = '0' if i % 2 == 0 else '1'
            if ch != expA:
                mismatchA += 1
            else:
                mismatchB += 1
        return min(mismatchA, mismatchB)