class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        el = None 

        for i in range(0,n):
            if cnt == 0:
                cnt = 1
                el = nums[i]
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        return el
        