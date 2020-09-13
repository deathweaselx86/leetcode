from math import ceil

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summation = 0
        dimension = len(mat)
        # what are the properties of the numbers on the diagonals?
        # if it is the primary diagonal, the next number will be at arr[i][i], i=0, i++, i < mat.length
        # for the second diagonal, the next number will be at arr[i][j], j = dim - 1, j --, j > -1, j = 0, j++, i=0, i++, i < mat.length
        # where do these intersect? arr[ceil(n/2)][ceil(n/2)] for n = mat.length
        j = dimension - 1
        for i in range(dimension):
            summation += mat[i][i]
            if i != j:
                summation += mat[i][j]
            j=j-1
        return summation