# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):

        def inorder_traversal(root: TreeNode):
            if root != None:
                inorder_traversal(root.left)
                self.arr.append(root.val)
                inorder_traversal(root.right)
        
        self.arr = []
        self.index = -1
        self.length = -1
        inorder_traversal(root)
        self.length = len(self.arr)

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        if self.index + 1 < self.length:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
