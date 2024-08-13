#We needed to check if the trees with root q and p are the same or not. This Code had Problems by solving the other trees on Leetcode when trying to submit but passes the three test cases

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        plist = []
        qlist = []

        def qfunc(Node):
            try:
                qlist.append(Node.val)
            except AttributeError:
                qlist.append(-1)

        def pfunc(Node):
            try:
                plist.append(Node.val)
            except AttributeError:
                plist.append(-1)
                


        qfunc(q)
        qfunc(q.left)
        qfunc(q.right)
        pfunc(p)
        pfunc(p.left)
        pfunc(p.right)

        if plist == qlist:
            return True
        else:
            return False
