class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        curr1 = l1
        curr2 = l2

        res = None
        start = None

        carry_over = False
        while curr1 is not None or curr2 is not None or carry_over:
            curr_num = 0
            if carry_over:
                curr_num += 1
                carry_over = False

            if curr1 is not None:
                curr_num = curr_num + curr1.val
                curr1 = curr1.next

            if curr2 is not None:
                curr_num = curr_num + curr2.val
                curr2 = curr2.next

            if curr_num >= 10:
                carry_over = True
                curr_num = curr_num - 10
            
            if res is None:
                res = ListNode(curr_num)
                start = res
            else:
                res.next = ListNode(curr_num)
                res = res.next

        return start

'''
Very simply, just iterate through both lists on 3 conditions, advance them both by 1 each time.
curr1 or curr2 or carry_over

Relatively straight forward problem overshadowed by the fact I misread the "reversed" condition.
'''
        
