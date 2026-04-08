class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for digit in nums:
            if digit not in nums_dict:
                nums_dict[digit] = 1
            else:
                return True
        return False