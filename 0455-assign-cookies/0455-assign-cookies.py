class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g = sorted(g)
        s = sorted(s)


        m = len(s)
        n = len(g)
        l,r = 0,0
    
        while l < m and r < n:
            if g[r] <= s[l]:
                r = r + 1
            l += 1
        return r
        