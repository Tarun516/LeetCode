
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            currentNode = stack.pop()
            if currentNode:
                res.append(currentNode.val)
                stack.append(currentNode.right)
                stack.append(currentNode.left)
        return res