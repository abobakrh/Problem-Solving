
class Solution(object):
    def numJewelsInStones(self, J, S):
        counter = 0
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_map = dict()
        for char in J:
            jewels_map[char] = 0  # entery for each char

        for char in S:
            if char in jewels_map.keys():  # exists
                jewels_map[char] += 1

        for (key, value) in jewels_map.items():
            if value != -1:
                counter += value

        return counter
