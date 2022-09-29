#  作者： 孙北晨
#  时间： 2022/3/17 16:00
#  介绍：
import doctest


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self):
        self.root = None
        self.height_hash = {}

    def sortedArrayToBST(self, nums):
        pass

    def insert(self, nums):
        """
        >>> avl = AVLTree()
        >>> avl.insert([3,1,2,4,5])
        >>> avl.root.val
        3
        >>> avl.root.left.val
        1
        """
        for num in nums:
            self.insert_not_balance(num)

    def preOrder(self):
        """
        >>> avl = AVLTree()
        >>> avl.insert([3,1,2,4,5,0])
        >>> avl.preOrder()
        [3, 1, 0, 2, 4, 5]
        """
        ret = []
        self.preOrder_helper(self.root, ret)
        return ret

    def preOrder_helper(self, root, ret):
        if not root:
            return
        ret.append(root.val)
        self.preOrder_helper(root.left, ret)
        self.preOrder_helper(root.right, ret)

    def insert_not_balance(self, x):
        """
        >>> avl = AVLTree()
        >>> avl.insert_not_balance(2)
        >>> avl.insert_not_balance(1)
        >>> avl.insert_not_balance(3)
        >>> avl.insert_not_balance(4)
        >>> avl.root.val
        2
        >>> avl.root.left.val
        1
        >>> avl.root.right.val
        3
        """
        self.root = self.insert_not_balance_helper(x, self.root)

    def insert_not_balance_helper(self, x, root):
        if not root:
            root = TreeNode(x)
            return root
        if x > root.val:
            root.right = self.insert_not_balance_helper(x, root.right)
        elif x < root.val:
            root.left = self.insert_not_balance_helper(x, root.left)
        else:
            print("不允许插入重复节点")
        return root

    def leftLeftRotation(self, root):
        """
        """
        left = root.left
        root.left = left.right
        left.right = root
        self.height_hash[root] = max(self.get_height(root.left), self.get_height(root.right)) + 1
        self.height_hash[left] = max(self.get_height(left.left), self.get_height(left.left)) + 1
        return left

    def get_height(self, node):
        """
        递归实现自动记录节点高度
        # >>> avl = AVLTree()
        # >>> avl.root = TreeNode(5)
        # >>> avl.root.left
        :param node:
        :return:
        """
        if not node:
            return 0
        elif node in self.height_hash:
            return self.height_hash[node]
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    avl = AVLTree()
    avl.insert_not_balance(2)
    avl.insert_not_balance(1)
    avl.insert_not_balance(3)
    avl.insert_not_balance(4)
    print(avl.root.val)
