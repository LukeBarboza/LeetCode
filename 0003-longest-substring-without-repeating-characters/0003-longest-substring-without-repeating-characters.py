class Solution:
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        if len(s) == 0:
            return 0
        
        number_dictionary = dict.fromkeys( set(s), -1)
        string_keys = list(number_dictionary.keys())
        indexes_list = []
        
        substring_length = 1
        old_substring_length = 1
                    

        
        while len(s) > 0:
            for j in range(len(string_keys)):
                current_char_idx = s.find(string_keys[j])
                if current_char_idx != -1:
                    indexes_list.append(current_char_idx)
            indexes_list.sort()
            s = s[1:]
            
            for k in range(len(indexes_list)-1):
                if indexes_list[k] + 1 is indexes_list[k+1]:
                    substring_length = substring_length + 1
                    if substring_length > old_substring_length:
                        old_substring_length = substring_length
                else:
                    substring_length = 1
                
            substring_length = 1
            indexes_list.clear()
        
            
        return old_substring_length