class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            queue_length = len(queue)
            level_order = []
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    level_order.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_order:
                result.append(level_order)
        return result