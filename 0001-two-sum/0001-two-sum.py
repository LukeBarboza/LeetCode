class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dic = {}
        list_of_indexes = []
        
        for i in range(len(nums)):
            # if nums[i] > target:
            #     continue
            
            rest = target - nums[i] 
            
            found_value = num_dic.get(rest)
            
            if found_value is not None:
                list_of_indexes.append(i)
                list_of_indexes.append(found_value)
                break
            
            num_dic.update({nums[i]: i})
            
        return list_of_indexes

   
            