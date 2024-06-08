class Solution(object):
    def frequencySort(self, s):

        shm = {}
        for char in s:
            shm[char] = shm.get(char, 0) + 1
        
        sorted_chars = sorted(shm.keys(), key=lambda x: shm[x], reverse=True)
        
        sorted_string = ''
        for char in sorted_chars:
            sorted_string += char * shm[char]
        
        return sorted_string