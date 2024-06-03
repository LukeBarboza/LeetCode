class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        result = [0] * n
        index = n - 1

        while left <= right:
            left_val, right_val = abs(nums[left]), abs(nums[right])
            if left_val > right_val:
                result[index] = left_val ** 2
                left += 1
            else:
                result[index] = right_val ** 2
                right -= 1
            index -= 1

        return result
        