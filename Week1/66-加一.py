class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        while digits and digits[-1] == 9:
            digits.pop()
            l.append(0)
        if not digits:
            return [1] + l
        else:
            digits[-1] += 1
            return digits + l