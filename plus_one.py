class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if not digits[i-1]:
                    digits.insert(0,1)
                    break
        if n == 0:
            digits.append(1)
        return digits