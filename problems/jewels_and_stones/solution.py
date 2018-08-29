class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num_stones = 0
        for stone in S:
            for jewel in J:
                if stone == jewel:
                    num_stones += 1
        return num_stones