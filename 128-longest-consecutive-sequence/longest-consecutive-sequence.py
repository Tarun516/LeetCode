class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        longest_length = 0
        
        for value in values:
            if value - 1 in values:
                continue
                
            current_length = 1
            next_value = value + 1
            
            while next_value in values:
                current_length += 1
                next_value += 1
                
            longest_length = max(longest_length, current_length)
            
        return longest_length
