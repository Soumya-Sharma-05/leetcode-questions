class Solution(object):
    def preorderTraversal(self, root):
        def helper(node):
            if not node:
                return
            result.append(node.val)  
            helper(node.left)        
            helper(node.right)       

        result = []
        helper(root)
        return result
