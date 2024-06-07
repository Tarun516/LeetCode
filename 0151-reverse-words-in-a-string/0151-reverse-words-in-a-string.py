class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        a = s.split()
        a = a[::-1]
        ans = ''
        for i in range(len(a)):
            ans += a[i] 
            if i < len(a) - 1:
                ans += " "
        
        return ans
            
        
        