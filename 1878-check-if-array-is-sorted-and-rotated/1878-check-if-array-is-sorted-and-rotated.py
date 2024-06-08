class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k = 1
        temp = sorted(nums)
        
        for _ in range(len(temp)):
            temp = temp[k:] + temp[:k]
            if temp == nums:
                return 1 
        return 0
 