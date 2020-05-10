class Solution(object):
    def firstUniqChar(self, s):
        char_map = OrderedDict()
        for char in s:
            if char not in char_map.keys():
                char_map[char] = 1
            else:
                char_map[char] += 1
        for item in char_map.keys():
            if char_map[item] == 1:
                return s.find(item)
        return -1
