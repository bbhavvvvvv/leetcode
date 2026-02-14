class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return min(1,poured)

        query_glass = min(query_glass, query_row - query_glass)
        dp = [poured] + [0] * (query_glass + 1)
        for r in range(query_row):
            end = min(r,query_glass)

            dp[end + 1] = 0.0

            next_lo, next_hi = 10**9, -1

            pouring = False

            for c in reversed(range(end + 1)):
                x = dp[c]
                if x > 1.0:
                    pouring = True
                    overflow = (x - 1.0) * 0.5
                    dp[c] = overflow
                    dp[c+ 1] += overflow

                    if c< next_lo: next_lo = c
                    if c> next_hi: next_hi = c
                    if c+ 1<= query_glass and c+ 1> next_hi : next_hi = c+ 1
                else:
                    dp[c] = 0.0

            if not pouring:
                return 0.0

            rem = query_row - (r+1)
            if query_glass < next_lo - rem or query_glass > next_hi + rem:
                return 0.0
        return min(1,dp[query_glass])        