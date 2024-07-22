# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#       / 1
#      /  |
#     / / | \
#    / 2 / \ 3  
#   |--|/   \|   

# Left -> Root -> Right 


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initializing array
        arr = []
        # defining helper function for inorder
        def inorder(root):
            # check of root available or not
            if not root :
                return
            # Traverse the left subtree
            inorder(root.left)
            # appending value to array visit of current node
            arr.append(root.val)
            # Traverse the right subtree
            inorder(root.right)
        # calling func for traversal
        inorder(root)
        # returning array
        return arr


# Time Complexity --    O(N)  as it traverse one time
# Space Complexity --   O(N)  as it use n extra space  