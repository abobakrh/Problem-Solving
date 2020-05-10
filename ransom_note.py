class Solution(object):
    def canConstruct(self,ransomNote, magazine):
        ransom_table = dict()
        magazine_table = dict()
        for char in ransomNote:
            if char != "":
                if char not in ransom_table.keys():
                    ransom_table[char] = 1
                else:
                    ransom_table[char] += 1
        for char in magazine:
            if char != "":
                if char not in magazine_table.keys():
                    magazine_table[char] = 1
                else:
                    magazine_table[char] += 1
        if ransomNote == magazine or ransomNote == "":
            return True
        for key in ransom_table.keys() :
            if key in magazine_table.keys():
                if magazine_table[key] < ransom_table[key]:
                    return False
            else :
                return False
        return True
