class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # flag = 0
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target :
                return i
            #     flag = i
            # elif nums[i] > target and nums[i-1] < target :
            #     flag = i
            # else :
            #     flag = len(nums)
        return len(nums)
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         nums.sort()
#         for i in range(n):
#                 if(nums[i] == target):
#                         return i
#         for i in range(n):
#                 if(nums[i]>target):
#                         return i     
#         for i in range(n):
#                 if(nums[i] != target):
#                         return n