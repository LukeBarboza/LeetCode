# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first_val = []
        second_val = []
        
        test = ListNode
        
        first_val.append(l1.val)
        second_val.append(l2.val)

        while l1.next is not None:
            l1 = l1.next
            first_val.append(l1.val)
        
        while l2.next is not None:
            l2 = l2.next
            second_val.append(l2.val)

        first_val.reverse()
        second_val.reverse()
        
        first_val = list(map(lambda x: str(x), first_val))
        second_val = list(map(lambda x: str(x), second_val))

        total = int("".join(first_val)) + int("".join(second_val))
        
        total_in_list = list(map(lambda x: int(x), str(total)))
        
        total_in_list.reverse()
        
        total_in_list = list(map(lambda x: str(x), total_in_list))
                
        l3 = ListNode(",".join(total_in_list))
        
        print(l3)
        
        return l3
        
        
        

