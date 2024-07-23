class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        f = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                nums[f+1] = nums[i]
                f+=1
                j +=1
        return j