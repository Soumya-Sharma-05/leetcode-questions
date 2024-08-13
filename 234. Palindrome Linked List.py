class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
    
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
    
        left, right = head, prev
        while right:  
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
    
        return True
