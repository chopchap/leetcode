class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    ancestor = root
    while True:
      if p.val < ancestor.val and q.val < ancestor.val:
        ancestor = ancestor.left
      elif p.val > ancestor.val and q.val > ancestor.val:
        ancestor = ancestor.right
      else:
        break
    return ancestor
