class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        left = len(arr) - 2
        right = len(arr) - 1
        max_right = arr[right]

        arr[right] = -1

        while left >= 0:
            current = arr[left]
            arr[left] = max_right

            if current > max_right:
                max_right = current

            left -= 1

        return arr