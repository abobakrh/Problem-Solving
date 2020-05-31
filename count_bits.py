class Solution:
    def countBits(self, num: int) -> List[int]:
        li = []
        for i in range(num+1):
             li.append("{0:b}".format(i).count("1"))
        return li
        