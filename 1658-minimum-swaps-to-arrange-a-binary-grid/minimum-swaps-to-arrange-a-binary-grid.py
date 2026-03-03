class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n, ans = len(grid), 0
        right1 = lambda x: x[:: -1].index(1) if 1 in x else n 
        zeros = list(map(right1,grid))

        for i in range(n):
            for j in range(i,n):
                if zeros[j] + 1 < n - i: continue
                zeros[i: j + 1] = [zeros[j]] + zeros[i: j]
                ans += j - i
                break
            else: return -1
        return ans