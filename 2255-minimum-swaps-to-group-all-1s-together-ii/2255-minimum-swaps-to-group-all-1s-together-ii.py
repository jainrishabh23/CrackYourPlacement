class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        w_s_count = nums.count(1)
        i = 0 
        l_1 = len(nums)
        if len(nums) != w_s_count:
            nums.extend(nums)
        length = len(nums)  

        start = 0
        end = w_s_count
        tot = sum(nums[start : end])
        maxi = tot

        while end < length:
            tot -= nums[start]
            tot += nums[end]
            start += 1
            end += 1
            maxi = max(tot, maxi)

        return w_s_count - maxi