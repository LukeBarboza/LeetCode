class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):

            remaining_value = target - nums[i]

            has_value = seen.get(nums[i], None) 
            
            if has_value is not None:
                return [int(has_value), i]

            seen[remaining_value] = i