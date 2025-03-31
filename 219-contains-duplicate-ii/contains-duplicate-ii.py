class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i in range(len(nums)):
            
            current_value = seen.get(str(nums[i]), None)

            if current_value:
                if current_value[0] == nums[i] and abs(i - current_value[1]) <= k:
                    return True
                seen[str(nums[i])] = [nums[i], i]

            else:
                seen[str(nums[i])] = [nums[i], i]


        return False