# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#      / 1- \
#     / /  \ \
#    / 2-/\ 3-\ 
#   |___/  \___|   

# Left -> Right -> Root


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initializing array
        arr = []
        # defining helper function for inorder
        def postorder(root):
            # check of root available or not
            if not root :
                return
            # Traverse the left subtree
            postorder(root.left)
            # Traverse the right subtree
            postorder(root.right)
            # appending value to array visit of current node
            arr.append(root.val)
        # calling func for traversal
        postorder(root)
        # returning array
        return arr


# Time Complexity --    O(N)  as it traverse one time
# Space Complexity --   O(N)  as it use n extra space 
        