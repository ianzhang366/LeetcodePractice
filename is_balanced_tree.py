# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # bfs nodes if the depth of the same level is not equal return false
        return self.treeDepth(root) >= 0

    def treeDepth(self, root):
        if root == None:
            return 0
        left = self.treeDepth(root.left)
        right = self.treeDepth(root.right)
        if left < 0 or right < 0 or abs(left-right) > 1 : #if goes to this section, then it will loop here all the time
            return -1
        depth = (max(left, right) + 1)
        return depth
