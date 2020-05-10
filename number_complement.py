class Solution(object):
    def findComplement(self, num):
        num_binary_string = "{0:b}".format(num)
        num_b_complement = ""
        for num in num_binary_string:
            if num == "0":
                num_b_complement += "1"
            else:
                num_b_complement += "0"
        return int(num_b_complement, 2)
