class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                count+=1
        return count <=1
        


# class Solution {
# public:
#     bool check(vector<int>& nums) {
#         int count=0;
#         for(int i=0;i<nums.size();i++){
#             if(nums[i]>nums[(i+1)%nums.size()])
#                 count++;
#         }
#         return (count<=1);
#     }
# };
