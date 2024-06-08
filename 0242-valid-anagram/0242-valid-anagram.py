class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        shm = {}
        thm = {}

        for char in s:
            if char in shm:
                shm[char] += 1
            else:
                shm[char] = 1
        for char in t:
            if char in thm:
                thm[char] += 1
            else:
                thm[char] = 1

        return shm == thm
        

            
            


        