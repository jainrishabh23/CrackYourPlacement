# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     /  -1
#    /  /   \
#   | -2    |-3     
#   |_______|

# Root -> Left -> Right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initializing array
        arr = []
        # defining helper function for preorder
        def preorder(root):
            # check of root available or not
            if not root :
                return
            # appending value to array visit of current node
            arr.append(root.val)
            # Traverse the left subtree
            preorder(root.left)
            # Traverse the right subtree
            preorder(root.right)
        # calling func for traversal
        preorder(root)
        # returning array
        return arr


# Time Complexity --    O(N)  as it traverse one time
# Space Complexity --   O(N)  as it use n extra space