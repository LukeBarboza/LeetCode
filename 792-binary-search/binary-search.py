class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo = 0
        hi = len(nums)

        while lo < hi:

            half_index = int((lo+hi)/2)

            if nums[half_index] == target:
                return half_index

            elif nums[half_index] < target:
                lo = half_index + 1
            
            else:
                hi = half_index

        return -1