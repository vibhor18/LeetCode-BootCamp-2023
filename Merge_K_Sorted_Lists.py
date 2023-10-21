lass Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        if(len(lists) == 0):
            return None
        if(len(lists) == 1):
            return lists[0]
        l1 = lists[0]
        l2 = lists[1]
        for i in range(1, len(lists)):
            if(i > 1):
                l1 = result
                l2 = lists[i]

            prehead = ListNode(-1)

            prev = prehead
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next            
                prev = prev.next

            prev.next = l1 if l1 is not None else l2

            result = prehead.next
        
        return result