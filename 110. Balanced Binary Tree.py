class Solution(object):
    def isBalanced(self, root):
        def check_height_balance(node):
            if not node:
                return True, -1
            
            left_balanced, left_height = check_height_balance(node.left)
            right_balanced, right_height = check_height_balance(node.right)
            
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            
            return balanced, height
        
        balanced, _ = check_height_balance(root)
        return balanced
