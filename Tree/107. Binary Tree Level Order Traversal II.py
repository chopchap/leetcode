class Solution:
  def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    levelOrder = []
    if not root:
      return levelOrder
    q = collections.deque([root])
    while q:
      level = []
      size = len(q)
      for _ in range(size):
        node = q.popleft()
        level.append(node.val)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      levelOrder.append(level)
    return levelOrder[::-1]
