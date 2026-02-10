class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        length = 0

        for i in range(n):
            odd = set()
            even = set()

            for j in range(i, n):

                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(odd) == len(even):
                    length = max(length,j-i+1)
        return length
        