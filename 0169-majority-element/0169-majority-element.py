import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # m = math.ceil(n)
        return nums[n//2]