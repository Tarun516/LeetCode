class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashset = {}

        for i in range(len(nums)):
            if nums[i] in hashset and abs(i - hashset[nums[i]]) <= k:
                return True
            hashset[nums[i]] = i
        return False
        

        