# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_queue = [p]
        q_queue = [q]
        print p_queue, q_queue
        while p_queue:
            if len(p_queue) != len(q_queue):
                return
            p_cur = p_queue.pop(0)
            q_cur = q_queue.pop(0)
            if p_cur == None and q_cur == None: 
                continue
            elif p_cur == None or q_cur == None:
                return False
            elif p_cur.val != q_cur.val:
                return False
            p_queue.append(p_cur.left)
            p_queue.append(p_cur.right)
            q_queue.append(q_cur.left)
            q_queue.append(q_cur.right)
        return True
