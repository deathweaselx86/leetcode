from collections import defaultdict


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = defaultdict(int)
        self.size = len(nums)
        for i, n in enumerate(nums):
            if n > 0:
                self.vector[i] = n
                

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum((self.vector[i] * vec.vector[i] for i in range(self.size) if vec.vector[i] and self.vector[i] ))
                
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)