class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        # f = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                nums[j] = nums[i]
                # f+=1
                j +=1
        return j

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         slow, fast = 0, 1
#         while fast in range(len(nums)):
#             if nums[slow] == nums[fast]:
#                 fast += 1
#             else:
#                 nums[slow + 1] = nums[fast]
#                 slow += 1
#                 fast += 1
#         return slow + 1
