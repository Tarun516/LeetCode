class Solution:
    def postorderTraversal(self, root):
        if not root: return []
        res = []
        if root.left: 
            res += self.postorderTraversal(root.left)
        if root.right:
            res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res