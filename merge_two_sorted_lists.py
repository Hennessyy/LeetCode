def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
         
    current = dummy = ListNode()
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1

    if l2:
        current.next = l2

    return dummy.next

        


print(mergeTwoLists([1,2,3],[1,2,3]))