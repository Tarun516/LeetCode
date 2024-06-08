class Solution:
    def isIsomorphic(self, s, t):
        return list(map(s.index,s)) == list(map(t.index,t))
