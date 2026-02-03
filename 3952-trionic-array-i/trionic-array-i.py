class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = 0 
        q = 0

        for i in range(1,len(nums) - 2):
            if nums[i - 1] < nums[i]:
                p = i
                continue
            break
        if p == 0:
            return False

        for i in range(p + 1,len(nums) - 1):
            if nums[i -1]> nums[i]:
                q = i
                continue
            break
        if q == 0 or q == len(nums) - 1:
            return False

        for i in range(q+1, len(nums)):
            if nums[i - 1] < nums[i]:
                continue
            else:
                return False
        return True