class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Iterate from the end of the string to the beginning
        for i in range(len(num) - 1, -1, -1):
            # Check if the current character is an odd digit
            if int(num[i]) % 2 != 0:
                # Return the substring from the start to the current position
                return num[:i + 1]
        # If no odd digit is found, return an empty string
        return ""

# Example usage
solution = Solution()
print(solution.largestOddNumber("35427"))  # Output: "35427"
print(solution.largestOddNumber("4206"))   # Output: ""
