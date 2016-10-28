# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #go through each node and switch it with a new node list
        node = ListNode(0)
        cur = head
        while cur:
            next_ = cur.next
            cur.next = node.next
            node.next = cur
            cur = next_
        return node.next

if __name__ == '__main__':
    s = Solution()

    # in_string = "abcabcbb"
    print s.reverseList(head)
