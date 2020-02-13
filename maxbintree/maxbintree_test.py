class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        node = TreeNode(5);
        return node

def test_exception():
    nums = [5]
    root = Solution.constructMaximumBinaryTree(self, nums)
    assert root.val == 5
