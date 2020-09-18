class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        array_length = len(arr)
        while i < array_length:
            if arr[i] == 0 and i < array_length:
                arr.insert(i+1, 0)
                i = i+1
            i = i+1
        del arr[array_length:]
