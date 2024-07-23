class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits.reverse()
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9 :
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
                # digits[n-1] = digits[n-1] + 1
        # digits.reverse()
        return [1]+digits
        