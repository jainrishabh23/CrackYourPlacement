class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # r = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    # r.append(i)
                    # r.append(j)
                    return [i,j]
        # return r