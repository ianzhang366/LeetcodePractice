# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        level = 1
        self.inOrder(root, level, result)
        return result

    def inOrder(self, root, level, result):
        '''
            in order means root, left, right to traversal the tree
        '''
        if root == None:
            return
        if level > len(result): # record the node information
            result.append([])

        result[level-1].append(root.val)
        if root.left != None:
            self.inOrder(root.left, level+1, result)
        if root.right != None:
            self.inOrder(root.right, level+1, result)
